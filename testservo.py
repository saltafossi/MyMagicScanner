import RPi.GPIO as GPIO
import time
import sys

#servoPin=18
miniServoPin=24

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	#GPIO.setup(servoPin,GPIO.OUT)
	GPIO.setup(miniServoPin,GPIO.OUT)

setup()

#servo=GPIO.PWM(servoPin,50)
miniServo=GPIO.PWM(miniServoPin,50)
miniServo.start(2.5)
time.sleep(1)

#servo.start(2.5)
#time.sleep(1.5)
#servo.stop()
miniServo.ChangeDutyCycle(7.5)
time.sleep(1)
miniServo.ChangeDutyCycle(2.5)

GPIO.cleanup()
