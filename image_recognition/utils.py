import numpy as np

def hex_to_dec(hex):
    return int(hex.replace("#", ""), 16)

def hex_to_3d(hex):
    hex = hex.replace("#", "")
    rgb = hex[:2], hex[2:4], hex[4:6]
    return np.array(list(map(lambda hex_color: int(hex_color, 16) / 255., rgb)))


def hex_embedding_similarity(hex, hex2):
    return np.sum(np.abs(hex - hex2)) / len(hex)
