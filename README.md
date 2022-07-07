# IoT_humidor_project


## Overview 
### Name and credentials: 
Johan Axell, ja225ik. Christopher Andersson, ca223sq. 

### Individual Contributions
In every step of the project, each aspect have been worked on jointly. Everything from hardware setup to coding to this report. 

### Short project overview
For this project, the goal is to compose a solution which enables surveillance of environment variables through different sensors. The different variables that will be looked at are the amount of light present, the temperature and the air humidity. These three are the core things to look at in regards to ideal cigar storage conditions. Acceptable ranges for these variables are pre-defined and any deviation from these will trigger a notification sent by email. 

### How much time it may take to do (approximation)
2 hours

## Objective
### Background for chosen project
We both have a great interest in and enjoy cigars. This project along with the sensors included in the firmware that was purchased presented a great oppurtunity to combine this interest and IoT. A humidor, which usually is a box or sometimes a whole room, is something that is primarly used for cigar storage and can often be acquired for a relative decent price. However this solution makes it possible to use other storage enviroments as well, as long as the variable ranges that are set are adhered to.

### Project purpose
The purpose is a combination of familiarization with the building of an IoT-solution along with facilitation in regards to monitoring different enviroment variables. 

### Project insights
This project and course has definitely provided great new knowledge in regards to basic IOT concepts, along with programming in Python. It has also given us some new insights in to how to use pybytes and ubidots for data analytics and visualization. These application builders are further discussed below. 

## Material
### List of material needed, including description, price and where to buy. 

**Disclaimer:** The material used in the projects were purchased as part of the LNU - 1DT305 Tillämpad IoT - FiPy and sensors bundle. However most of what's included is not used which is why we would suggest the option below. However if one were to be interested in the extras thats included in the bundle, it can be purchased at electrokit.com 

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

You can do this either by cloning the repository (instructions can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).) or by pressing “Code” and then “Download ZIP”. Place the files in to a directory.

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


* Keep in mind that this is done with the Pysense board alone, the FiPy should not be mounted on it. <br/>
* Keep DFU-util and the firmware in the same directory. <br/>
* In Zadig, if you can't find your device, you can click on "Options" and then on "List all devices". 
* In DFU mode the Product ID of the device is changed.  Below you can see the Product ID for the Pysense board in update mode and application(normal) mode. 

![image](https://user-images.githubusercontent.com/90699893/177196667-a71a29a8-d607-4899-9de2-1557c043012a.png)


Download links: <br/>
* Latest firmware DFU file: [here](https://software.pycom.io/findupgrade?key=pysense2.dfu&type=all&redirect=true) <br/>
* DFU-Util [here](http://dfu-util.sourceforge.net/releases/dfu-util-0.9-win64.zip) <br/>
* Zadig [here](https://zadig.akeo.ie/) <br/>

### Open the project in Atom
Press "Add folders" and choose the directory that holds the project files. <br/>
Now you can upload the project to the device by pressing CTRL + ALT + S. <br/>
To run the selected file you press CTRL + ALT + R. <br/>

## Putting everything together
For the sake of simplicity and not making things more complicated than they have to be, we have chosen not to use a breadboard, extra wiring or any external sensors for this project. The hardware is more than capable of handling the temperature and environment for the intended area of use. The needed sensors are included in the expansion board as well. 

However, for further exploration and added functionality, or to look into how the connection between the microcontroller and sensor shield should be set up,  information can be found [here] (https://pycom.github.io/pydocs/gettingstarted/connection/fipy.html#third)

## Chosen platform
For the duration of this project, multiple platform options for data- analysis, visualization and storage were explored. For obvious reasons, the first one that was looked at was Pybytes. Pybytes is a device management platform specifically made for pycom devices. At first, considering our low level of knowledge in the field of IoT, this seemed like a good idea. Even though we experienced some issues initially, we soon had our device provisioned and connection to pybytes established. 

However, we soon realized that we wanted to challenge ourselves a bit more, which meant that having pybytes handle everything related to the MQTT-protocol under the hood was not something that we were interested in. Even if setting up our own broker and MQTT-connection still was an option using pybytes, the platform lacked the possibility to set up alerts or prompts based on the sensor data which eventually made us explore other options. 
Secondly, we looked into Adafruit.io. However, the need for paying for premium in order to access the features we looked for, combined with the fact that we couldn’t determine whether or not the platform supported our microcontroller made us look elsewhere. 

Eventually, we stumbled upon Ubidots which turned out to be what we were looking for. Like Adafruit, there is a premium membership which included some neat functionality that will be elaborated on in a later section. However, for our project, the basic membership level was more than enough. Unlike Pybytes, Ubidots offered the possibility to set up triggers based on sensor data values which in turn would result in an email or a text message. This was a crucial part of the project considering the implication of values outside the specified range. The overall impression was that the user friendliness was one step above the one experienced with pybytes, the functionality was to easier grasp and the options for data visualization was a lot more visually pleasing. 


Below is a screenshot of the device menu on the Ubidots platform. This is where the different sensor variables are defined. 
![bild](https://user-images.githubusercontent.com/71591829/177188185-902a6842-4cfc-402d-88dc-9621c04417d8.png)



## The code

### Libraries
Initially we included everything from [Pycoms pysense2 library]( https://github.com/pycom/pycom-libraries/releases/download/v2.0.0/pysense2.zip/) but we decided to remove modules that were outside of our scope and to only keep those parts that were needed for our project.
We chose to create a separate module called config and to store our WiFi credentials along with our Ubidots token there. We did this because it allows us to share our project while keeping that kind of sensitive information hidden by for example adding a .gitignore rule for it. <br/>
![image](https://user-images.githubusercontent.com/90699893/177204263-75255c6d-5841-4957-87ea-de7f480fb2f9.png)

### Avarage temperature 
We thought that it might be interesting to know the average temperature and to achieve this we used the three variables counter, avgtemp and final_avg as shown below. Counter is incremented by one, avgtemp calculates avgtemp plus the value from the temperature sensor and final_avg is avg_temp divided by counter. These calculations are done once every iteration but the information is only sent once every fourth iteration through our usage of the modulus operator. <br/>
![image](https://user-images.githubusercontent.com/90699893/177204309-ce9d888c-a232-4717-8fa1-1fc56bc528e3.png)

### Troubleshooting
While testing our code we came to realize that there was no way for the device to know if the data was being received by Ubidots. We were curious to know what the response code was when we, for example, inserted the wrong token. In that case was it was 401, which is the status code which is usually returned when the client provides no credentials or invalid credentials. This is very helpful for troubleshooting. 
![image](https://user-images.githubusercontent.com/90699893/177204378-82d13fba-2b38-452c-9225-b34fc4367fd8.png)


## Data transmission and connectivity
### Frequency
We have chosen to send data every 30th minute. The main reason why is because we assume that if this were to leave the development stage, a battery would be included and this would be one way to save power. We believe that uploading more often than this would not provide any obvious benefits but uploading more seldom might compromise the enviroment quality in the case of some sort of malfunction or unforseen circumstance. 
<br/>
![bild](https://user-images.githubusercontent.com/71591829/177195839-4366899c-cedd-4cbd-b88f-86aad4356bad.png)
<br/>
If a battery isn't connected however, the "DELAY"-variable could be lowered without any downsides. 
### Wireless protocols used
For our project, we have chosen to use Wi-Fi as the wireless protocol. We have done so due to it being easily accessible and compared to another option such as LoRa, the improved data transfer distance is not something that would benefit our project anyhow. It is however worth considering options when taking battery life into consideration and how Wi-Fi in general consumes quite a bit more power. Another aspect worth noting is that the device will almost exclusively be used indoors, which increases the chance of a Wi-Fi being available. LTE is another option we briefly looked into but chose to skip. If the data was of a more sensitive nature and security would be an aspect of higher priority, this could be a more probable candidate. 

Along with defining the variables and importing the library, this code snippet highlights the main functionality for establishing the Wi-Fi connection.  Heavily inspired by: https://hackmd.io/@lnu-iot/Hkpudaxq9

![bild](https://user-images.githubusercontent.com/71591829/177198191-3bd54c49-95a8-4ef5-b255-7e48d46cd68a.png)

### Transport protocols used

In regards to transport protocols, we eventually ended up with HTTP instead of MQTT. The main reason for this was actually because we had some previous experience with MQTT and wanted to explore HTTP and how it works. However, in our project there is quite a few aspects indicating that MQTT would be just as good, if not an even better choice. To mention a few, MQTT is designed for data delivery and not entire pages as HTTP. Security wise, MQTT also has a slight edge due to it using SSL/TLS while also applying encryption to the payload. This while HTTP offers no encryption at all. MQTT offers a slightly higher level of reliability as well. 

In the code snippet below is our main functionality for creating a json object and sending it through a POST-request. 
Again, heavily inspired by: https://hackmd.io/@lnu-iot/Hkpudaxq9

![bild](https://user-images.githubusercontent.com/71591829/177203824-9b51f3ac-3f3c-4adb-9323-9fa73216056f.png)



## Data presentation
### Dashboard
![image](https://user-images.githubusercontent.com/90699893/177205492-817a59ba-6a13-4e42-94cc-76bbaea0d525.png)
The dashboard contains the following: 
* Temperature – in Celsius (Thermometer with custom color logic, green if within the range of 18-23 degrees, otherwise red)
* Temperature – in Fahrenheit (Thermometer with custom color logic, green if within the * range of 64-73 degrees, otherwise red) 
* Average temperature in Celsius over time
* Temperature over time
* Light – Lux value (Gauge with custom color logic, green if within the range of 0-100 lux, otherwise red)
* Light over time
* Relative Humidity – Percentage (Gauge with custom color logic, green if within the range of 60-70, otherwise red) 
* Humidity over time

### Database

With a Ubidots STEM (free) account data is stored for 1 month. The data could be exported to for example Google Sheets or as a .CSV file, which means it could be stored for a longer period of time. Data is saved as often as it is uploaded, which in our case is every 30th minute for temperature, humidity and lux values and every two hours for average temperature values. We decided that this was enough and therefore we did not research other database alternatives for this project.

### Data triggers
When the event is triggered, an e-mail is sent to our e-mail.
We added the following triggers: 
* Humidity is too low (Humidity is below 60 for 5 minutes)
* Humidity is too high (Humidity is greater than 70 for 5 minutes)
* Avarage temperature is too low (Avarage temperature is below 18 for 5 minutes)
* Avarage temperature is too high (Avarage temperature is greater than 23 for 5 minutes)
* Environment is too bright (Light lux value is greater than 100 for 5 minutes)


Without a paid subscription we were unable to add conditionals such AND or OR. Had we been able to add conditionals we would've combined the triggers for humidity in to one trigger and the ones for temperature in to another, like so: Humidity is below 60 for 5 minutes OR Humidity is greater than 70 for 5 minutes.


## Finalizing the design
Overall, the project ended up quite close to how we envisioned the finalized product. Our goal with the project was to facilitate collection of data through sensors and the presentation of data, using application builders such as Ubidots, along with establishing a wireless connection between client and server. 

The project, and course overall, provided a heap of new valuable experiences and lessons, a long with a new and interesting way of problem solving. Battling with firmware updates in the pysense expansion board is unlike anything we encountered previously. 

![bild](https://user-images.githubusercontent.com/71591829/177514602-ad703515-8298-4e09-a347-84b33f06bb24.png)

![bild](https://user-images.githubusercontent.com/71591829/177514650-762155da-a548-45c4-95ca-9492db22df4c.png)


To mention a few things that we probably will change moving forward. 
We will include a battery to make the usage of the device a lot more practical. We have already looked into how it would work and have the code prepared for it. 
We also aim to actually integrate a lot of this into an app or webpage instead, especially now when we are a bit more familiarized with HTTP.  Having a prompt regarding the temperature being too high sent through email isn’t ideal compared to a notification in an app downloaded in your smartphone. The data presentation would be another thing that would be moved here as well. 

It would also be nice to expand on the code that was briefly discussed in the Troubleshooting section so that we can be made aware of other response codes. This in order to further facilitate and streamline troubleshooting. This could potentially incorporate different LED flashing from the FiPy depending on the current error status. 

Another thing worth mentioning if we we’re to re-do the project is that we would probably purchase more suitable parts. The bundle included a lot of things that we did not need which in turn just ended up being somewhat of a waste. To mention a few, adding a breadboard, wiring and another temperature sensor, when there is one already present on the sensor shield did not make any sense at all. The same could be said for the other sensors as well. 

