from picamera import PiCamera
from time import sleep

# Initialize the camera
camera = PiCamera()

# Adjust camera settings if needed
camera.resolution = (1280, 720)  # Set the resolution (width, height)
camera.rotation = 180           # Rotate the image (in degrees)

# Wait for the camera to warm up
sleep(2)

# Capture an image
camera.capture('/home/pi/image.jpg')  # Specify the output file path

# Release the camera resources
camera.close()