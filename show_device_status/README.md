# check-device-[online/offline]-status

Now it supports checking the [online/offline] status of registered devices in linklab.metadata (or linklab.inlux) according to the certain device types
- Awair Omni
- LightLevel
- Temp Humidity Sensor (TempHumidity)
- LoRa Temp Humidity Sensor
- Door Sensor
- Setra Power Battalion 48

The naming convention of the device type used above is followed by [linklab.metadata](https://metadata.linklab.virginia.edu/)

Please refer to [influx_python_interface:Part 2](https://github.com/AustinFengYi/uva-linklab-influx/blob/main/influx_python_interface.ipynb) to have more details about the bascis and implementation.

<img width="700" alt="2nd sensor temp humid" src="https://github.com/AustinFengYi/uva-linklab-influx/assets/22648364/0f71cd8f-e25e-47f5-8a78-f1cc8406b9ac"> 


## QuickStart
### Prerequisites
#### Versioning: in requirements.txt
- python==3.8.5
- influxDB==1.8.4
- influxdb-client==1.19.0 (This API support 1.8.4 version)
- pandas
- decouple

## How to Run the Program 
### Check the [online/offline] status 
- First, please access [linklab.metadata](https://metadata.linklab.virginia.edu/) to get full information of all devices registered in the metadata so far
- After that, you should also have access to get link lab sensor data from [influx.linklab](https://infrastructure.linklab.virginia.edu/linklabcloud/index.html)

Run the command according to the certian device type
