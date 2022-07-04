# IoT_humidor_project


## Overview 
### Name and credentials: 
Johan Axell, ja225ik. Christopher Andersson, ca223sq. 

### Short project overview
For this project, the goal is to compose a solution which enables surveillence of enviroment variablables through different sensors. The different variables that will be looked at are the amount of light present, the temperature and the air humidity. These three are the core things to look at in regards to ideal cigar storage conditions. Acceptable ranges for these variables are pre-defined and any deviation from these will trigger a notification sent by email. 

### How much time it make take to do (approximation)
1 hour

## Objective
### Background for chosen project
A long going interest of cigars have always existed in the family. This project along with the sensors included in the firmware that was purchased presented a great oppurtunity to combine this interest and IoT. A humidor, which usually is a box or sometimes a whole room, is something that is primarly used for cigar storage and can often be acquired for a relative decent price. However this solution makes it possible to use other storage enviroments as well, aslong as the variable ranges that is set are adhered to.

### Project purpose
The purpose is a combination of familiarization with the building of an IoT-solution along with facilitation in regards to monitoring different enviroment variables. 

### Project insights
This project and course have definetly provided great new knowledge in regards to basic IOT Concepts, along with programming in python. It has also given me some new insights regarding how to use pybytes and ubidots for data analytics and visualization. These application builders are further discussed below. 

## Material
### List of material needed, including description, price and where to buy. 

**Disclaimer:** The material used in the projects were purchased as part of the LNU - 1DT305 Tillämpad IoT - FiPy and sensors bundle. However most of what's included isnt used which is why I would suggest the option below. However if one were to be interested in the extras thats included in the bundle, it can be purchased at electrokit.com 

| First Header  | Category | Purchased at | Price |
| ------------- | ------------- | ------------- | ------------- |
| FiPy 1.0 | Micro controller  | sparkfun.com  | 77,95 USD  |
| Pycom Pysense 2.0X  | Expansion board/Sensor shield  | sparkfun.com  | 34,95 USD  |
| Micro-USB*  | Cable  |   |   |

* Micro-USB had been acquired before project started. 



FiPy 1.0  ![bild](https://user-images.githubusercontent.com/71591829/177190781-16972770-a004-4529-b23e-5e7a1962930b.png)
Fipy is one of the latest Micropython enabled microcontrollers, made by Pycom. It has integrated multiple network options, specifically WiFi, Bluetooth, LoRa, Sigfox and dual LTE-M. However in order to program it, the device also needs an expansion board in order to use its serial port. This is one of the reasons why we are also using a PySense 2.0X. Worth noting is also that it can handle temperatures from -20 to 85 degrees celcius. This is crucial considering we are not using any external sensors for this project. It also has a very low power usage compared to other micro controllers. 



PySense 2.0X  ![bild](https://user-images.githubusercontent.com/71591829/177190888-53d089f1-9637-467c-af55-123e5e99c77c.png)
The expansion board is a sensor shield and offers a micro-USB port along with multiple sensors. Outside the sensors that are used in this project, it also offers a pressure sensor, an accelerometer , battery charger and microSD card compatibility. 


## Computer setup

### Download our project:

You can do this either by cloning the repository (instructions can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).) or by pressing “Code” and then “Download ZIP”. 

![image](https://user-images.githubusercontent.com/90699893/177184189-e95fbb42-11e9-4ce6-a766-2c2fbd581957.png)

### Setting up the development environment:

Atom was our integrated development environment (IDE) of choice for this project. To use it you need to download and install Atom along with Node js. You will also need to install a plugin called Pymakr within Atom.
Within Atom, press CTRL + Comma, this will open the settings page in which you press “Install”, search for “pymakr”, and then press “Install” as shown below: 
 
![image](https://user-images.githubusercontent.com/90699893/177182534-518097f1-8b8e-4dbe-8a3c-d0ea5df97f58.png)

It has been announced that Atom will be retired on December 15, 2022. Therefore, for posterity, we would like to inform that you can also use Visual Studio Code.  

Visual Studio Code can be downloaded here. 
In Visual Studio Code, press CTRL + Shift + X, this will open the Extensions page in which you search for “pymakr” and then press “Install” as shown below. 

![image](https://user-images.githubusercontent.com/90699893/177182600-7c351a63-8989-4ad8-a7f4-2d9830a66331.png)

### Firmware Update

Pycom recommends that firmware is upgraded to the latest version as they are constantly making improvements and adding new features to the devices. 
You can download the latest firmware from [this]( https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true) link.
Install the downloaded file and then tick the box saying “Start Pycom Firmware Updater after finishing installation” and then press “Finish” 
You can press “Continue” past the first two screens. Under “Please select the serial port to use” you choose the COM port for your PyCom Expansion board. If you are unsure you can find this information in Windows Device Manager. Länka in bild från Windows Device Manager.
In the same screen, after “Type:” choose development. If you wish to use Pybytes instead of Ubidots (we will elaborate on the difference between these two further down in the text), you can choose pybytes here.
In the next screen, tick all of the boxes (Erase during update, CONFIG partition and NVS Partition) and press continue. After it is done you press "Done".


### Expansion Board Firmware Update
The expansion board needs to be updated as it is required by one of the libraries used for this project. Without this firmware update we were getting no values from the light sensors.
This is the most complicated aspect of setting up this project.  We therefore advise that you read the following tutorial carefully and that you don’t try to rush through the process of updating the expansion board. 
The tutorial that we followed is linked [here](https://docs.pycom.io/updatefirmware/expansionboard/), but we will provide some key information here to assist you.

Normally the expansion board is in Application mode but when we want to update the firmware we need to put the board in DFU (Device Firmware Upgrade) mode as this allows altering of the device’s firmware. In DFU mode the Product ID of the device is changed.  Below you can see the Product ID for the Pysense board in update mode and application(normal) mode. 

![image](https://user-images.githubusercontent.com/90699893/177196667-a71a29a8-d607-4899-9de2-1557c043012a.png)

 
Download links: <br/>
Latest firmware DFU file: [here](https://software.pycom.io/findupgrade?key=pysense2.dfu&type=all&redirect=true) <br/>
DFU-Util [here](http://dfu-util.sourceforge.net/releases/dfu-util-0.9-win64.zip) <br/>
Zadig [here](https://zadig.akeo.ie/) <br/>

Keep in mind that this is done with the Pysense board alone, the FiPy should not be mounted on it. <br/>

Keep DFU-util and the firmware in the same directory. <br/>


### How the code is uploaded
### Steps that needs to be completed in regards to new softwares and driver updates. 

## Putting everything together
### Circuit diagram

## Chosen platform
For the duration of this project, multiple platform options for data- analysis, visualization and storage was explored. For obvious reasons, the first one that was looked at was Pybytes. Pybytes is a device management platform specifically made for pycom devices. At first, considering the low level of knowledge in the field of IoT, this seemed like a good idea. Even though we experienced some issues initially, we soon had our device provisioned and connection to pybytes established. 

However, we soon realized that we wanted to challenge ourselves a bit more, which meant that having pybytes handle everything related to the MQTT-protocol under the hood was not something that we were interested in. Even if setting up our own broker and MQTT-connection still was an option using pybytes, the platform lacked the possibility to set up alerts or prompts based on the sensor data which eventually made us explore other options. 
Secondly, we looked into Adafruit.io. However, the need for paying for premium in order to access the features we looked for, combined with the fact that we couldn’t determine whether or not the platform supported our microcontroller made us look elsewhere. 

Eventually, we stumbled upon Ubidots which turned out to be what we were looking for. Like Adafruit, there is a premium membership which included some neat functionality that will be elaborated on in a later section. However, for our project, the basic membership level was more than enough. Unlike Pybytes, Ubidots offered the possibility to set up triggers based on sensor data values which in turn would result in an email or a text message. This was a crucial part of the project considering the implication of values outside the specified range. The overall impression was that the user friendliness was one step above the one experienced with pybytes, the functionality was to easier grasp and the options for data visualization was a lot more visually pleasing. 


Below is a screenshot of the device menu on the Ubidots platform. This is where the different sensor variables are defined. 
![bild](https://user-images.githubusercontent.com/71591829/177188185-902a6842-4cfc-402d-88dc-9621c04417d8.png)



## The code

## Data transmission and connectivity
### Frequency
We have chosen to send data every 30th minute. The main reason why is because we assume that if this were to leave the development stage, a battery would be included and this would be one way to save power. We believe that uploading more often than this would not provide any obvious benefits but uploading more seldom might compromise the enviroment quality in the case of some sort of malfunction or unforseen circumstance. 
<br/>
![bild](https://user-images.githubusercontent.com/71591829/177195839-4366899c-cedd-4cbd-b88f-86aad4356bad.png)
<br/>
If a battery isn't connected however, the "DELAY"-variable could be lowered without any downsides. 
### Wireless protocols used
For our project, we have chosen to use Wi-Fi as the wireless protocol. We have done so due to it being easily accessible and compared to another option such as LoRa, the improved data transfer distance is not something that would benefit our project anyhow. It is however worth considering options when taking battery life into consideration and how Wi-Fi in general consumes quite a bit more power. Another aspect worth noting is that the device will almost exclusively be used indoors, which increases the chance of a Wi-Fi being available. LTE is another option we briefly looked into but chose to skip. If the data was of a more sensitive nature and security would be an aspect of higher priority, this could be a more probable candidate. 

Along with defining the variables and importing the library, this code snippet highlights the main functionality for establishing the Wi-Fi connection. Credit to https://hackmd.io/@lnu-iot/Hkpudaxq9

![bild](https://user-images.githubusercontent.com/71591829/177198191-3bd54c49-95a8-4ef5-b255-7e48d46cd68a.png)



### Transport protocols used
### Design choices(Kanske radera)

## Data presentation
### Dashboard
### Database
### Data triggers

## Finalizing the design


