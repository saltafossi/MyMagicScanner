#from PIL import Image
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import sys

print(1)
camera = PiCamera()
print(2)
set_name = sys.argv[1]
print(3)
def camera_setup(camera):
	camera.color_effects = (128,128)
	camera.rotation = 90
	camera.resolution = (300,100)
print(4)
camera_setup(camera)
print(5)

timestamp=time.strftime("%Y%m%d%H%M%S")
camera.capture(set_name+"/"+set_name+"_"+timestamp+".jpg")
print("Picture Taken! See {0}_{1}.jpg!"+format(set_name,timestamp))

print(6)