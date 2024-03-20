from gpiozero import Motor
from time import sleep

# Define the motor
motor = Motor(forward=17)
motor.forward()


