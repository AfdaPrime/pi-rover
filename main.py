from flask import Flask, render_template
from gpiozero import Motor
from time import sleep

app = Flask(__name__)

# Define the motor with forward and backward pins
motor = Motor(forward=17, backward=18)

# Flag to indicate if motor is currently running
motor_running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward')
def forward():
    global motor_running
    motor_running = True
    motor.forward()
    return 'Motor moved forward'

@app.route('/backward')
def backward():
    global motor_running
    motor_running = True
    motor.backward()
    return 'Motor moved backward'

@app.route('/stop')
def stop():
    global motor_running
    motor_running = False
    motor.stop()
    return 'Motor stopped'

@app.route('/status')
def status():
    return 'Motor is running' if motor_running else 'Motor is stopped'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
