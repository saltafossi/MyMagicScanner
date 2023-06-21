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

# Start PWM with 0% duty cycle (servo at 0 degrees)
pwm.start(0)

try:
    while True:
        # Move the servo to 0 degrees
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        
        # Move the servo to 90 degrees
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        
        # Move the servo to 180 degrees
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)

except KeyboardInterrupt:
    # Stop PWM and clean up GPIO
    pwm.stop()
    GPIO.cleanup()