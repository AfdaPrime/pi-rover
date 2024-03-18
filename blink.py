from gpiozero import LED
from time import sleep

# Define the GPIO pin number for the LED
led_pin = 17

# Create an LED object
led = LED(led_pin)

# Blink the LED
while True:
    led.toggle()  # Toggle the LED on/off
    sleep(5)      # Wait for 1 second
