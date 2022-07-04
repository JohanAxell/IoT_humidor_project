import urequests as requests
import machine
import time
import pycom
import config as co

from network import WLAN
from pycoproc import Pycoproc
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01

TOKEN = co.token # Add token string from ubidots to config.py
DEVICE_LABEL = "fibyboard" # Device name from Ubidots
VARIABLE_TEMP = "temperature"  # Variable name from ubidots
VARIABLE_HUMID = "humidity"  # Variable name from ubidots
VARIABLE_LIGHT = "light"  # Variable name from ubidots
AVG_TEMP = "avgtemp" # Variable name from ubidots
WIFI_SSID = co.ssid_name # Enter name of Wifi-network to config.py
WIFI_PASS = co.ssid_passw # Enter password of Wifi-network to config.py
DELAY = 1800  # Seconds between uploads to ubidots, 1800 = every 30th minute.
counter = 0 # Used to determine how often to upload the averages
avgtemp = 0 # Variable for average temperature

py = Pycoproc() # Instatiation of pycoproc library
if py.read_product_id() != Pycoproc.USB_PID_PYSENSE: # Checking if pysense expansion board is connected
    raise Exception('Not a Pysense')

# WiFi connection
wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)
try:
    wlan.connect(WIFI_SSID, auth=(WLAN.WPA2, WIFI_PASS), timeout=5000)
    while not wlan.isconnected ():
        machine.idle() # energy saving while waiting
    print("\nConnected to " + WIFI_SSID.upper() + ".\n")
except Exception:
    print('\nCould not connect to '+ WIFI_SSID.upper() +', going back to sleep.\n')
    py.setup_sleep(5) # Sleep for 5 seconds
    py.go_to_sleep() # Initiate sleep state

# instatiation of libraries
si = SI7006A20(py)
lt = LTR329ALS01(py)

# set your battery voltage limits here, remove comment if using battery
# vmax = 4.2
# vmin = 3.3
# battery_voltage = py.read_battery_voltage()
# battery_percentage = (battery_voltage - vmin / (vmax - vmin))*100
# print("Battery voltage: " + str(py.read_battery_voltage()), " percentage: ", battery_percentage)

# builds json to be used for http post request
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None


# Sending data to Ubidots Restful Webservice
def sendData(device, variable, value):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)
        if data is not None:
            print("Uploading " +variable+ ": " + str(value))
            req = requests.post(url=url, headers=headers, json=data)
            if req.status_code == 401:
                print("Upload failed, check token information")
            return req.json()
        else:
            pass
    except:
        pass
# Calling sendData to upload as often as decided in DELAY-variable.
while True:
    # Extract value from sensors
    tempvalue = si.temperature()
    humidvalue = si.humidity()
    lightvalue = lt.lux()

    counter = counter+1
    avgtemp = (avgtemp + tempvalue)
    final_avg = avgtemp / counter

    sendData(DEVICE_LABEL, VARIABLE_LIGHT, lightvalue)
    sendData(DEVICE_LABEL, VARIABLE_TEMP, tempvalue)
    sendData(DEVICE_LABEL, VARIABLE_HUMID, humidvalue)
    if counter % 4 == 0: # Only uploads each 4th iteration
        sendData(DEVICE_LABEL, AVG_TEMP, final_avg)
    time.sleep(DELAY) # Time before next upload
