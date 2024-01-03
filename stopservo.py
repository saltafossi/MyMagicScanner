import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin used for the servo
servo_pin = 24

# Set up the GPIO pin for output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance with frequency 50Hz
pwm = GPIO.PWM(servo_pin, 50)

pwm.start(0)
time.sleep(2)
pwm.ChangeDutyCycle(0)
time.sleep(0.5)
pwm.stop()
GPIO.cleanup()