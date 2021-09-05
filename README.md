# Radio
Old radio refurbishment

## Project Description

I'm refurbishing the following 1954 radio:<br/>
<img src="images/Radio_general_view.jpg" width="500"/>

At the end of the project, the radio can:
- Play (up to 9) webradios from different countries (up to 5), for a total of 45 webradios
- Pair and then stream bluetooth from smarthpone
- Listen music from  a 3.5mm jack connector input

The radio has 4 buttons:
- A [voltage selector](/images/radio_voltage_selector.jpg) at radio rear which will be used to select radio langage. A position change when bluetooth mode is activated result in bluetooth pairing
- A [5 position switch selector](/images/radio_left_buttons.jpg) at radio bottom left: the selector is tuned to select only three positions for the 3 mode: webradio, bluetooth, jack 
- A [6 position switch selector](/images/radio_right_button.jpg): to select the different webradio
- A [ON/OFF/potentiometer button](/images/radio_left_buttons.jpg) at radio upper left: to switch ON/OFF radio adn to change volume

The radio has 2 "brain":
- A [Teensy2](https://www.pjrc.com/store/index.html) (equivalent to arduino nano) to read positions of buttons thanks to digital output and analog input
- A [Raspberry Pi 4 2Gb](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/). With a python script, the raspberry:
  * Read informations coming from teensy (via USB)
  * Launch [VLC](https://www.videolan.org/vlc/index.html) to stream webradio or to listen jack input
  * Pair bluetooth devices
  * Stream bluetooth music coming from devices
  * Output the sound to an [Hifiberry Amp 2](https://www.hifiberry.com/shop/bundles/hifiberry-amp2-bundle-4/)

To highlight best parts of the radio, several LEDs powered by Teensy have been installed (see night results on [front image](/images/radio_leds_on.jpg) and [rear image](/images/radio_leds_on_2.jpg)):
- Inside each lamp
- Inside the 2 aluminium block
- Next to rear a voltage selector to see what voltage is selected

## Hardware description

The following synoptic presents links between main hardware parts:<br/>
<img src="images/Synoptic_hardware_radio.jpg" width="500"/>
<br/>For memory (or to duplicate the project), schematics showing each connection between Teensy and selectors/buttons/LEDs are below presented:<br/>
<img src="images/teensy_hardware_schematic.png" width="1000"/>
The main principle to detect the position of each switch (performed by teensy software) is the same as a **matrix keyboard**: 
1. A 5V is generated on teensy pin B0, B1 & B2 being @ 0V
2. Eeach Teensy Input Voltage (F0, F1, F4) is read.
 - If 5V is read on F0, position In_1 is selected. Else another position is selected.
 - If 5V is read on F1, position In_1 is selected. If 2.5V is read on F1, position In_4 is selected. Else another position is selected.
 - If 5V is read on F4, position In_1 is selected. If 2.5V is read on F4, position In_4 is selected. Else another position is selected.
3. A 5V is generated on teensy pin B1, B0 & B2 being @ 0V
4. Eeach Teensy Input Voltage (F0, F1, F4) is read.
 - If 5V is read on F0, position In_2 is selected. Else another position is selected.
 - If 5V is read on F1, position In_2 is selected. If 2.5V is read on F1, position In_5 is selected. Else another position is selected.
 - If 5V is read on F4, position In_2 is selected. If 2.5V is read on F4, position In_5 is selected. Else another position is selected.
5. A 5V is generated on teensy pin B2, B0 & B1 being @ 0V
6. Eeach Teensy Input Voltage (F0, F1, F4) is read.
 - If 5V is read on F0, position In_3 is selected. Else another position is selected.
 - If 5V is read on F1, position In_3 is selected. Else another position is selected.
 - If 5V is read on F4, position In_3 is selected. If 2.5V is read on F4, position In_6 is selected. Else another position is selected.
7. The teensy software restart @ step 1

## Software Description
### Teensy Software

The code has 3 functions: 
- Get the position of the 3 selector
- Get the value of the volume potentiometer
- Switch ON/OFF the front blue Lamp randomly during 1.2s. This function is to perform an visual effect when changing radio

To access to these function from Raspberry Pi, the serial communication is used and the following commands have to be send to Teensy (with "\n" at the end of the command):
- "status" to get selector positions
- "volume" to get potentiometer value
- "lumiere" to perform the visual effect

### Raspberry Pi Software
