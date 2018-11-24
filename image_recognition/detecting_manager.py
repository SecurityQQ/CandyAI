from time import time
from color_extractor import predict_color


class DetectingManager:
    def __init__(self):
        pass

    def parse_frame(self, frame, detected_entities):
        for entity_name, entity_bound in detected_entities.items():
            if entity_name == "person":
                pass # detect cloths
            elif entity_name == "backpack":
                pass #detect color


