from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

from pprint import pprint


app = ClarifaiApp(api_key='9a2117f4967a4f2d92e84adb221c5cc1')

# get the general model
model = app.models.get("demographics")

# predict with the model
with open("/Users/aleksandrmalysev/Yandex.Disk.localized/Developer/CandyRobot/img/2018-11-24 18:29:16.640477.jpg", "rb") as file:
    image = ClImage(file_obj=file)
    prediction = model.predict([image])

    pprint(prediction)