from influxdb import InfluxDBClient
from decouple import config
from datetime import datetime
import pandas as pd
import arrow
from pathlib import Path

class Influx():
    def __init__(self):
        self.user = config('INFLUXDB_USERNAME')
        self.password = config('INFLUXDB_PASSWORD')
        self.host = config('INFLUX_HOST')
        self.dbname = config('INFLUXDB_DATABASE_NAME') # 'linklab-users' or 'gateway-generic' 
        self.port = 443
        self.ssl = True
        self.client = self.get_client()
    
    def get_client(self):
        client = InfluxDBClient(host=self.host, port=self.port, username=self.user,
                                password=self.password, database=self.dbname, ssl=self.ssl)
#         print('Retrieving client for: %s' % dbname)
        self.client = client
        return client
    
    def __str__(self):
        return str(self.__class__.__dict__)

    def get_device_query_adds(self, device_id_list):
        q_append = ''
        count = 0
        for device_id in device_id_list:
            if count == 0:
                q_append += 'and ("device_id"=\'%s\'' % device_id
            else:
                q_append += 'or "device_id"=\'%s\'' % device_id
            count += 1
        q_append += ')'
        return q_append
    
    def get_result_set(self, fieldname, add_param):  # show in new readme
        q_str = 'SELECT * FROM "%s" WHERE %s' % (fieldname, add_param)
#         print(q_str)
        client = self.client
        result_set = client.query(q_str)
        return result_set
    
    def get_result_set_from_custom_q_str(self, q_str):
        print(q_str)
        client = self.client
        result_set = client.query(q_str)
        return result_set
    
    def convert_influx_time_to_datetime(self,time_str, timezone):
        t = arrow.Arrow.strptime(time_str[:19], '%Y-%m-%dT%H:%M:%S')
        return t.to(timezone).datetime  # utc.to('local').datetime
    
    def get_longform_df(self,result_set, timezone='US/Eastern'):
        # essentially converting the result set to long_form
        df = pd.DataFrame([pt for pt in result_set.get_points()])
        # convert the string time to datetime objects
        if 'time' in df.columns:
            df['time'] = df['time'].map(
                lambda x: self.convert_influx_time_to_datetime(x, timezone))
            return df
        else:
            return None
    
    
    # Access current (now()) timing value
    """ upload rate: 
    +------+------------+------------+---------------+--------------------+-------------+--------------------------+
    | Type | Awair Omni | LightLevel | Temp Humidity | LoRa Temp Humidity | Door Sensor | Setra Power Battalion 48 | 
    +------+------------+------------+---------------+--------------------+-------------+--------------------------+
    | Rate |   10s      |  30 min    |    15 min     |       05 min       |   20 min    |         1 min            |
    +------+------------+------------+---------------+--------------------+-------------+--------------------------+   
    """
    
    def get_time_query_from_now(self, device_type):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lookup = {
            "Awair" : "time > now() -1m ",
            "Light_Level": "time > now() -40m ",
            "Temp_Humid": "time > now() -20m ",
            "LoRa_Temp_Humid": "time > now() -15m ",
            "Door_Sensor":"time > now() -30m ",
            "Setra_Power_Battalion_48":"time > now() -6h ",
        }
#         print("Current Time:", current_time)
        tq = lookup.get(device_type, None)
        return tq    

def get_sensor_data(fieldname, device_id, device_type):
    x = Influx()
    a = x.get_time_query_from_now(device_type)
#     print('Retrieving device: %s, field: %s' % (device_id,fieldname))
    if device_id is not None:
        a += x.get_device_query_adds([device_id])
    r = x.get_result_set(fieldname, a)
    
    if x.get_longform_df(r) is None:
        # return None if there is no data after querying from influx
        return None 
    else: 
        # get the latest one if there is data
        return x.get_longform_df(r).tail(1) 

# +------+------------+------------+---------------+--------------------+-------------+--------------------------+
''' Pseudo: A Python interface to check device_status in the Link Lab
For registered devices in linklab.metadata (linklab.influx), I want to know if devices' status from a certain type are on-or-off
    1. Get all devices that you request according to the device type
    2. Data Query from influx
    3. The retun after the query will be 'status_on_list' and 'status_off_list'

'''
# +------+------------+------------+---------------+--------------------+-------------+--------------------------+

filepath = Path('../influx_devices_exported.csv')
df = pd.read_csv(filepath)

# Device Mapping
# defining the device_types , MAC_Address <-> device_type
device_ids_lookup = {
    "Awair" : ["70886b"],
    "Light_Level": ["0506"],
    "Temp_Humid": ["018a","018317c3"],
    "LoRa_Temp_Humid": ["24E124136D"],
    "Door_Sensor": ["0591e","0591f","05920","01834", "01833", "0181"],
    "Setra_Power_Battalion_48": ["ELEUV0202"],
}

check_field_from_device_lookup = {
    "Awair" : "Temperature_°C",
    "Light_Level": "Illumination_lx",
    "Temp_Humid": "Temperature_°C",
    "LoRa_Temp_Humid": "Temperature_°C",
    "Door_Sensor": "rssi",
    "Setra_Power_Battalion_48": "voltage_v",
}

# +------+------------+------------+---------------+--------------------+-------------+--------------------------+
''' Step 1: Get all devices that you request according to the device type
'''
def get_influx_devices_from_type(device_type):
    res = {}
    for idx , row in df.iterrows():
        for device_id_lookup in device_ids_lookup[device_type]:
            if device_id_lookup in row["Sensorid"]:
            # For now, 'type' is not a tag in influx
                res[row["Sensorid"]] = {"device_id":row["Sensorid"], "type": row["Type"]  ,"location_specific":row["LocationSpecific"], "description": row["Description"]  } 
    return res
# 
# +------+------------+------------+---------------+--------------------+-------------+--------------------------+
''' Step 2. Data Query from influx 
    Step 3. The retun after the query will be 'status_on_list' and 'status_off_list'
'''
def check_device_act_status(device_type):
    on_devices = {}
    off_devices = {}
    certain_devices = get_influx_devices_from_type(device_type)
#     print(certain_devices)
    print(f"Number of device type [{device_type}] in linklab.metadata: {len(certain_devices)}")
    for device in certain_devices:
        qs = get_sensor_data(check_field_from_device_lookup[device_type], device, device_type ) 
        if qs is None:
            off_devices[device] = {"device_id":device, "type": certain_devices[device]["type"]  ,"location_specific":certain_devices[device]["location_specific"], "description": certain_devices[device]["description"] ,'value':None, } 
#             off_devices[device]= {  'value':None, }
        else:
            on_devices[device] = {"device_id":device, "type": certain_devices[device]["type"]  ,"location_specific":certain_devices[device]["location_specific"], "description": certain_devices[device]["description"] ,'value':qs['value'].to_string(index=False) } 
#             on_devices[device]= {  'value':qs['value'].to_string(index=False)}
    
    return on_devices, off_devices
# 
