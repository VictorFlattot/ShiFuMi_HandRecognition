import cv2
import numpy as np
from IPython.display import display, Image

#Open a connection to the webcam
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Perform image processing using OpenCV if needed
        cv2.imshow('Webcam', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted")

finally:
    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()