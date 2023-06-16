import cv2

# Initialize the USB camera
camera = cv2.VideoCapture(0)  # Use index 0 for the first USB camera

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Failed to open the camera")
    exit()

# Capture a frame from the camera
ret, frame = camera.read()

# Check if the frame was captured successfully
if not ret:
    print("Failed to capture frame")
    exit()

# Save the captured frame as an image file
cv2.imwrite('image.jpg', frame)

# Release the camera resources
camera.release()