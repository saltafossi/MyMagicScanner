import RPi.GPIO as GPIO
import time
import sys

servoPIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

args = sys.argv

p = GPIO.PWM(servoPIN, 50) # GPIO 24 for PWM with 50Hz
p.start(0) # Initialization
time.sleep(2)
p.ChangeDutyCycle(float(args[1]))
time.sleep(2)
p.stop()
GPIO.cleanup()