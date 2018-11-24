import numpy as np
import cv2


def hex_to_dec(hex):
    return int(hex.replace("#", ""), 16)

def hex_to_3d(hex):
    hex = hex.replace("#", "")
    rgb = hex[:2], hex[2:4], hex[4:6]
    return np.array(list(map(lambda hex_color: int(hex_color, 16) / 255., rgb)))


def hex_embedding_similarity(hex, hex2):
    return np.sum(np.abs(hex - hex2)) / np.sum(np.abs(hex) + np.abs(hex2) + 1e-24)


def smooth_image(path):
    img = cv2.imread(path)
    smoothed_img = cv2.GaussianBlur(img, (21, 21), 0)
    cv2.imwrite(path, smoothed_img)


def get_colors_distibution(path):
    img = cv2.imread(path)

get_colors_distibution("/Users/aleksandrmalysev/Yandex.Disk.localized/Developer/CandyRobot/image_recognition/withoutface.png")