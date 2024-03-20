from gpiozero import Motor
from time import sleep

# Define the motor with forward and backward pins
motor = Motor(forward=17, backward=18)


# Move the motor forward
motor.forward()
    
  


