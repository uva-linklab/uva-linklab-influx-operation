import base
import json
# insecure-requestwarnings-be-disabled-in-the-requests-module
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# +------+------------+------------+---------------+--------------------+-------------+--------------------------+
''' Step 1: Get all devices that you request according to the device type
Example: Get all devices in linklab.metadata with Type: Awair
REFERENCES:
    https://metadata.linklab.virginia.edu/                                       
'''

device_type = "Awair" 
res = base.get_influx_devices_from_type(device_type)
print(f"Number of device type [{device_type}] in linklab.metadata: {len(res)}")
print(json.dumps(res, indent=4,sort_keys=True))


# +------+------------+------------+---------------+--------------------+-------------+--------------------------+
''' Step 2. Data Query from influx 
    Step 3. The retun after the query will be 'status_on_list' and 'status_off_list'
Example: Check Device_type: Awair
'''
device_type = "Awair"
status_list = base.check_device_act_status(device_type)

# ON status
print("+------+------------+------------+---------------+--------------------+")
print(f"Amount of 'ON status' {device_type} device: {len(status_list[0])}")
print(json.dumps(status_list[0], indent =4, sort_keys=True))


# OFF status
print("+------+------------+------------+---------------+--------------------+")
print(f"Amount of 'OFF status' {device_type} device: {len(status_list[1])}")
print(json.dumps(status_list[1], indent =4, sort_keys=True))
# +------+------------+------------+---------------+--------------------+-------------+--------------------------+

