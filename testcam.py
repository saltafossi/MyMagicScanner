import pygame.camera
import pygame.image
from PIL import Image 


def capture_image(camera_device, output_path):
    pygame.camera.init()
    cameras = pygame.camera.list_cameras()

    if camera_device not in cameras:
        print(f"Camera device '{camera_device}' not found.")
        return

    #cam = pygame.camera.Camera(camera_device, (640, 480))
    cam = pygame.camera.Camera(camera_device, (1280, 960))
    cam.start()

    image = cam.get_image()
    #pygame.image.save(image, output_path)
    data = pygame.image.tostring(image, 'RGB')
    pil_img = Image.frombytes('RGB', image.get_size(), data)
    pil_img.save(output_path)
    pil_img.close

    cam.stop()
    pygame.camera.quit()

    print(f"Image saved to: {output_path}")

# Set the camera device (change this according to your setup)
camera_device = "/dev/video0"

# Set the output path for the captured image
output_path = "captured_image.jpg"

# Capture and save the image
capture_image(camera_device, output_path)