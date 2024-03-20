from flask import Flask, render_template
from gpiozero import Motor
from time import sleep

app = Flask(__name__)

# Define the motor with forward and backward pins
motor = Motor(forward=17, backward=18)

@app.route('/')
def index():
    motor.stop()
    return render_template('index.html')

@app.route('/forward')
def forward():
    motor.forward()
    return 'Motor moved forward'

@app.route('/backward')
def backward():
    motor.backward()
    return 'Motor moved backward'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


from app import app

if __name__ == '__main__':
    # Run the Flask app on all network interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)