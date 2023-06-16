from PIL import Image
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import sys

camera = PiCamera()
set_name = sys.argv[1]

def camera_setup(camera):
	camera.color_effects = (128,128)
	camera.rotation = 90
	camera.resolution = (300,100)

camera_setup(camera)

while True:
	timestamp=time.strftime("%Y%m%d%H%M%S")
	camera.capture(set_name+"/"+set_name+"_"+timestamp+".jpg")
	print "Foto fatta {0}_{1}.jpg!"+format(set_name,timestamp)
	time.sleep(3)

