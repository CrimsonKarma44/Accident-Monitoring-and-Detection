import requests
import cv2
import os, time

URL = "http://192.168.179.89:8000/camera/"
# Set the folder where images will be saved
save_folder = "static/captured_images"


# Headers (optional, but often required by APIs)
headers = {
    'Content-Type': 'text/plain'
}


# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
# , cv2.CAP_DSHOW
# Change the index to match your external webcam (default is 0, external is usually 1 or higher)
cap = cv2.VideoCapture(2)  # Try 1, 2, or higher if 0 doesn't work

if not cap.isOpened():
    print("Error: Could not open external webcam.")
    exit()

image_count = 0  # Counter for saved images

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    print(type(frame))
    
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the video feed
    # cv2.imshow("External Webcam", frame)

    # Check for key presses
    # key = cv2.waitKey(1) & 0xFF
    
    # if key == ord('s'):  # Press 's' to save an image
    image_count += 1
    image_path = os.path.join(save_folder, f"image_{image_count}.jpg")
    cv2.imwrite(image_path, frame)
    print(f"Image saved: {image_path}")
    # Open the image
    with open(image_path, "rb") as img_file:
        # files = {"file": image_path.encode()}
        # data = {"coordinates": "12.3456, 78.9101", "region": "city-name"}
        response = requests.post(URL, data=image_path, headers=headers)
    
    time.sleep(1)
    print(response.json())
    # elif key == ord('q'):  # Press 'q' to quit
    #     break

# Release the webcam and close windows
cap.release()
# cv2.destroyAllWindows()



