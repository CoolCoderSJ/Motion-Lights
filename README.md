# Motion Lights
This project uses a [Gesture Sensor [Grove]](https://wiki.seeedstudio.com/Grove-Gesture_v1.0/) attached to a [Wio Link](https://wiki.seeedstudio.com/Wio_Link/). The Wio Link connects to a server and relays the live readings from the sensor. Separate code ([main.py](/blob/main/main.py)) runs on a server 24/7 listening for readings from the wio link.

You can view a demo of the system [here](https://github-production-user-asset-6210df.s3.amazonaws.com/53063247/258203569-f08c90f3-39ea-4d36-9513-83d9adacc334.mp4)

The gesture sensor is able to track 6 different directions, which means it can track whether a person has left the room or entered it, and adjust the lights based on how many people are in the room.

The lightbulbs used are [Tuya Smart Bulbs](https://expo.tuya.com/product/1075067). They can be adjusted for any smart bulb that allows code to interface with them, official or otherwise.

Notes:
- The Wio Link is a $7 (USD) ESP8266 API based microcontroller. The grove interface is proprietary to SeeedStudio devices. However, you can get the [Raspberry Pi Grove Hat](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/) or the [Arduino Grove-Mega Shield](https://wiki.seeedstudio.com/Grove-Mega_Shield/) to interface with the gesture sensor through a Raspberry Pi or Arduino.
- The Wio Link is EOL. The android APK may be available online, but the app is no longer available for iOS. 
