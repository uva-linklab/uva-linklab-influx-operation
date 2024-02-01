# uva-linklab-influx-operation
For now, this program handles the linklab.influx operation in Python with the following implementations
- Part1: A python interface to access Living Link Lab data
- Part2: A Python interface to check device_status in the Link Lab according to certain device (or called sensor) type
##
Please refer [Link Lab Cloud](https://infrastructure.linklab.virginia.edu/linklabcloud/index.html) to have more information about how Link Lab metadata is designed and works, and refer [linklab.metadata](https://metadata.linklab.virginia.edu/)
 to get a list of existing registered devices in linklab metadata
##
Subsequently, please refer [influx_python_interface.ipynb](https://github.com/AustinFengYi/uva-linklab-influx/blob/main/influx_python_interface.ipynb) to have more information about how I implemented the program in Python to 
1. Query link lab influx data
2. Check certain devices' [online/offline] status  

Also, the Python file program is implemented in [show_device_status](https://github.com/AustinFengYi/uva-linklab-influx-operation/tree/main/show_device_status) directory to specifiaclly describe how to check [online/offline] status from each of certain devices' type. Currently, the following device type has been implemented.
- Awair Omni
    - [`Humidity_%`, `Temperature_°C`, `awair_score`, `pm2.5_μg/m3`, `co2_ppm`, `voc_ppb`, `battery_%`]
    - [Rate: 10sec]
- LightLevel
    - [`Illumination_lx`, `rssi`]
    - [Rate: 30min]
- Temp Humidity Sensor (TempHumidity)
    - [`Humidity_%`, `Temperature_°C`]
    - [Rate: 15min]
- [LoRa Temp Humidity Sensor](https://nam1.cloud.thethings.network/console/applications/uva-engineers-way-sensors)
    - [`Humidity_%`, `Temperature_°C`]
    - [Rate: 5min]
- Door Sensor
    - [`rssi`, `Contact`]
    - [Rate: 20min]
- Setra Power Battalion 48
    - [`voltage_v`]
    - [Rate: 1min]
- [LoRa Water Ultrasonic Sensor](https://nam1.cloud.thethings.network/console/applications/dl-mbx)
    - [`voltage_v`]
    - [Rate: 1min]
- [LoRa Water Pressure Sensor](https://nam1.cloud.thethings.network/console/applications/dl-pr-26)
    - [`voltage_v`]
    - [Rate: 1min]


<img width="700" alt="2nd sensor temp humid" src="https://github.com/AustinFengYi/uva-linklab-influx/assets/22648364/738a110c-2ee5-4de1-96b2-1e25f3d375f5"> 
<img width="700" alt="2nd senseeeor temp humid" src="https://github.com/AustinFengYi/uva-linklab-influx/assets/22648364/2fa94d35-d12e-497b-8caf-6baa3c280827"> 

## 
The result from [influx_python_interface.ipynb: Part 2](https://github.com/AustinFengYi/uva-linklab-influx/blob/main/influx_python_interface.ipynb) / directory [show_device_status](https://github.com/AustinFengYi/uva-linklab-influx-operation/tree/main/show_device_status) would be as below.

| Awair Omni | LightLevel |
| -------- | -------- | 
| <img width="481" alt="截圖 2023-11-24 上午9 39 22" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/af2f69c2-15fc-4d78-ae5e-c928a6df9c64">   |<img width="527" alt="截圖 2023-11-24 上午9 46 30" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/d811341e-285c-4a2f-8188-0f772cf58fd1">|   
| <img width="458" alt="截圖 2023-11-24 上午9 54 20" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/d4ad27a2-d11e-429d-af5d-983b57d9822e">  |  <img width="459" alt="截圖 2023-11-24 上午10 00 45" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/1279f789-b5f0-4b32-a707-72a523cfebfa">  | 
|<img width="468" alt="截圖 2023-11-24 上午9 54 35" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/31de8eb6-437a-4315-8883-59237278298c">|<img width="469" alt="截圖 2023-11-24 上午10 00 59" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/35c66e7b-fdec-478c-aa40-f75537ba2e36">|

| Temp Humidity Sensor | LoRa Temp Humidity Sensor |
| -------- | -------- | 
| <img width="501" alt="截圖 2023-11-24 上午9 46 41" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/31fde360-b461-49bd-91c8-46bbef2c86cc">   | <img width="619" alt="截圖 2023-11-24 上午9 49 37" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/68705eb2-b685-495e-ba9e-9a99c2e5f8ac">| 
|  <img width="438" alt="截圖 2023-11-24 上午9 58 08" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/08908ab1-f1a5-4bb0-b621-ca6e3c5ed4c3">|<img width="560" alt="截圖 2023-11-24 上午9 57 33" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/73a31a85-4472-458e-8771-d9d7002a68b1">|
|   |![截圖 2023-11-21 上午11 51 59](https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/fb01a6a4-415b-48a2-b9e6-426ce7433230)|

| Door Sensor | Setra Power Battalion 48 |
| -------- | -------- | 
|  <img width="480" alt="截圖 2023-11-24 上午9 50 43" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/c131bc4e-08f3-4153-9030-1c7585e4a896">  |<img width="453" alt="截圖 2023-11-24 上午9 50 56" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/b77b6c8a-7a71-4431-8dd7-42fe080d8a56">|    
|<img width="517" alt="截圖 2023-11-24 上午9 59 22" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/7c45d993-8638-429c-a826-57537f829a9e">|<img width="530" alt="截圖 2023-11-24 上午10 00 06" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/0ba3971c-3745-431b-9ac3-4ff6fa897314">|
|<img width="508" alt="截圖 2023-11-24 上午9 59 30" src="https://github.com/AustinFengYi/uva-linklab-influx-operation/assets/22648364/1ba8fc98-2216-4a80-becd-bc7565ab5092">|  |














