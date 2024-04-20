from flask import Flask, render_template
from gpiozero import Motor
from time import sleep

app = Flask(__name__)

# Define the motor with forward and backward pins
motor = Motor(forward=17, backward=18)
steer = Motor(forward=22, backward=23)

# Flag to indicate if motor is currently running
motor_running = False
steer_turned = False


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

@app.route('/left')
def left():
    global steer_turned
    steer_turned = True
    steer.forward()
    global motor_running
    motor_running = True
    motor.forward()
    return 'steer moved left'



@app.route('/right')
def right():
    global steer_turned
    steer_turned = True
    steer.backward()
    global motor_running
    motor_running = True
    motor.forward()
    return 'steer moved right'


@app.route('/stop')
def stop():
    global motor_running
    motor_running = False
    motor.stop()
    return 'Motor stopped'


@app.route('/straight')
def straight():
    global steer_turned
    steer_turned = False
    steer.stop()
    global motor_running
    motor_running = False
    motor.stop()
    return 'Steer stopped'

@app.route('/status')
def status():
    return 'Motor is running' if motor_running else 'Motor is stopped'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
