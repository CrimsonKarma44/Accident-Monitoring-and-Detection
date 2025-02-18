import cv2, datetime
import numpy as np

# Load YOLO model
net = cv2.dnn.readNet("static/model_files/rad_less.weights", "static/model_files/rad_less.cfg")

# Load the class labels
with open("static/model_files/rad_less.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


def ModelChecker(img:str) -> dict:
    response = {}
    # Load and preprocess the image
    # image = cv2.imread("static/img/putholes.jpeg")
    image = cv2.imread(img)
    image = cv2.resize(image, None, fx=0.4, fy=0.4)
    height, width= image.shape[:2]
    
    # height, width = image.shape[:2]                                                                                                                                                                                                   
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Set the input to the network
    net.setInput(blob)

    # Get output layer names

    # Run forward pass
    detections = net.forward(output_layers)

    # Process detections
    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w // 2
                y = center_y - h // 2
                response['x'] = x
                response['y'] = y
                response['w'] = w
                response['h'] = h
                response["datetime"] = str(datetime.datetime.now())
                response["type"] = classes[class_id]
                response["confidence"] = str(confidence)
    return response

# ModelChecker("/home/karma/Documents/code/projects/final/static/img/cracks.jpeg")