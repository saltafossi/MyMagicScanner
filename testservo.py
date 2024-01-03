import RPi.GPIO as GPIO
import time

servoPIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 24 for PWM with 50Hz
p.start(0) # Initialization
time.sleep(2)
try:
  while True:
    p.ChangeDutyCycle(13.5)
    time.sleep(3)
    p.ChangeDutyCycle(6.7)
    time.sleep(3)
except KeyboardInterrupt:
  time.sleep(0.5)
  p.ChangeDutyCycle(0)
  p.stop()
  GPIO.cleanup()