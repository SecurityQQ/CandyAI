from color_extractor import predict_color, detect_close_patter, get_message_by_picture

from clarifai.rest import ClarifaiApp
from pprint import pprint
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


app = ClarifaiApp(api_key='9a2117f4967a4f2d92e84adb221c5cc1')

me_in_red = "/Users/aleksandrmalysev/Yandex.Disk.localized/Скриншоты/2018-11-24_15-22-54.png"
guy_in_black = "/Users/aleksandrmalysev/Yandex.Disk.localized/Скриншоты/2018-11-24_15-36-32.png"


completely_black_guy = "http://allday2.com/uploads/posts/2017-09/1505131958_fotolia_81291012_subscription_xxl-kopirovat.jpg"
girl_like_unicorn = "https://pbs.twimg.com/profile_images/432888790399856640/egikGaN6_400x400.png"
yellow_green_guy = "http://anthocyanin1.ru/pics/781/colorsample-1.jpg"


with open(me_in_red, "rb") as f:
    c = get_message_by_picture(app, yellow_green_guy)
    print(c)