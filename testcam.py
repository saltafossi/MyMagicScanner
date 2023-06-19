import pygame
import pygame.camera

# Initialize Pygame and the camera module
pygame.init()
pygame.camera.init()

# Get a list of available cameras
cam_list = pygame.camera.list_cameras()

if not cam_list:
    print("No cameras found.")
    exit()

# Create a camera object
cam = pygame.camera.Camera(cam_list[0])

# Start the camera
cam.start()

# Set the desired resolution
width, height = 640, 480
cam.set_resolution(width, height)

# Initialize the Pygame display
screen = pygame.display.set_mode((width, height))

# Main loop for capturing and displaying frames
running = True
while running:
    # Capture a frame from the camera
    image = cam.get_image()

    # Display the frame on the screen
    screen.blit(image, (0, 0))
    pygame.display.flip()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Stop the camera
cam.stop()

# Quit Pygame
pygame.quit()