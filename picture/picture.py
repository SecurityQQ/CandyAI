from PIL import Image
from cv2 import *

import time

def start():
	cap = cv2.VideoCapture(0)

	while(True):
	    # Capture frame-by-frame
		ret, frame = cap.read()

	    # Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		# Write some Text

		font = cv2.FONT_HERSHEY_SIMPLEX
		frame = cv2.putText(frame, 'Press Q to get CandyPhoto', (150,450), font, 0.8, (20, 255, 0), 2, cv2.LINE_AA)

	    # Display the resulting frame
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			ret, frame = cap.read()
			imwrite("filename1.jpg",frame)
			cap.release()
			cv2.destroyAllWindows()
			break

	import Stitcher