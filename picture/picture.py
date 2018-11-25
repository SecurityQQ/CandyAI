from PIL import Image
from cv2 import *

import time


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()

    # Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		imwrite("filename1.jpg",frame)
		break

import Stitcher