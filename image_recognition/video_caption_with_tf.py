import cv2, pandas as pd
from datetime import datetime
import tensorflow as tf
from detect_objects import detect_objects

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")

video = cv2.VideoCapture(0)

df = pd.DataFrame(columns=["Start", "End"])
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
        print(objects)
        for k, v in objects.items():
            cv2.rectangle(frame, v[0], v[1], (125, 255, 51), thickness=2)

        cv2.imshow("frame", frame)

        if len(objects) > 0:
            print(objects)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()