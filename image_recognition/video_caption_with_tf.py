import cv2, pandas as pd
from datetime import datetime
import tensorflow as tf
from detect_objects import detect_objects
from detecting_manager import DetectingManager

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")

video = cv2.VideoCapture(0)

detecting_manager = DetectingManager()

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2




with tf.gfile.FastGFile('/Users/aleksandrmalysev/Downloads/ssd_inception_v2_coco_11_06_2017/frozen_inference_graph.pb',
                        'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

with tf.Session() as sess:
    # Restore session
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')

    while True:

        capture, frame = video.read()

        objects = detect_objects(frame, sess)

        properties = detecting_manager.parse_frame(frame, detected_entities=objects)
        properties = properties[0]
        print(properties)


        for k, v in objects.items():
            cv2.rectangle(frame, v[0], v[1], (125, 255, 51), thickness=2)

        caption = str(properties['color'])

        if "demography" in properties and len(properties['demography']) > 0:
            caption += " " + str(properties["demography"])

        cv2.putText(frame, caption,
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)
        cv2.imshow("frame", frame)


        # if len(objects) > 0:
        #     print(objects)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()