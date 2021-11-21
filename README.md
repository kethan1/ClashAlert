# ClashAlert

## Project Goal:

Crash Alert for self-driving cars by identifying traffic lights, moving cars, and pedestrians.

## Description: 

This project involves driving a robot car containing a Raspberry Pi. The car is demonstrative of a group of self-driving cars. 

The car tries to avoid a collision by detecting traffic lights and other objects like cars and pedestrians.

The controls are on a webpage with a joystick as well as a constant video stream that informs the user about what is in the path of the robot. If the user wants the car to stop, they will trigger a button that displays a series of red LEDs and the camera detects them using OpenCV. 

The joystick triggers the motors that move the robot in the direction that it is supposed to move towards. To avoid collisions, we have implemented an IR sensor that will detect objects ahead of the robot.

## Future Goals: 

We also envision that our plan will be enhanced when we transmit the signals among the cars via 5G localized network. We plan to broadcast the signal to other cars on the same path in order to ensure the safety of pedestrians. It will also be used for emergency vehicles so they have a constant feed of the best route.

## Hardware Used

- Raspberry Pi
- Jumper cables
- L298N
- Battery Pack
- IR Sensor
- Picamera
- Red LEDs
- Button
- Battery holders
- Yellow gear motors
