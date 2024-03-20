from gpiozero import Motor
from time import sleep

# Define the motor with forward and backward pins
motor = Motor(forward=17, backward=18)

try:
    # Move the motor forward
    motor.forward()
    
    # Wait for 2 seconds
    sleep(5)
    
    # Move the motor backward
    motor.backward()
    
    # Wait for 2 seconds
    sleep(5)

finally:
    # Stop the motor
    motor.stop()
