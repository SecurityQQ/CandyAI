from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

from pprint import pprint

def extract_demography(app, url):
    if app is None:
        app = ClarifaiApp(api_key='9a2117f4967a4f2d92e84adb221c5cc1')
    model = app.models.get("demographics")

    if isinstance(url, str):
        prediction = model.predict_by_url(url=url)
    else:
        image = ClImage(file_obj=url)
        prediction = model.predict([image])

    try:
        regions = prediction['outputs'][0]['data']['regions']

        for region in regions[:1]: ## analyse only first guy on the picture
            concepts = region['data']['face']
            age = sorted(concepts['age_appearance']['concepts'], key=lambda j: -j['value'])[0]['name']
            gender = sorted(concepts['gender_appearance']['concepts'], key=lambda  j: -j['value'])[0]['name']
            multiculture = sorted(concepts['multicultural_appearance']['concepts'], key=lambda j: -j['value'])[0]['name']
            result = {
                "age": age,
                "gender": gender,
                "multiculture": multiculture
            }
            return result
    except KeyError as e:
        return {}

if __name__ == "__main__":
    # with open("/Users/aleksandrmalysev/Yandex.Disk.localized/Developer/CandyRobot/image_recognition/2018-11-25 01:01:54.391514.png", "rb") as file:
    #     print(extract_demography(None, file))
    print(extract_demography(None, "https://downloader.disk.yandex.ru/preview/2232806c55b7b708fb8a34cd118a8f09de484b0faff89c591767cea3ccdf06c4/5bfa14b4/95QNuOT7MZ1p-kZH60-e39-aP-QcqQhuKGprQrfbNTtvF0osLwJTtXEYwpASL07Nzf2MsCp2FRvoqVpWTCE4Mg%3D%3D?uid=0&filename=2018-11-25_01-18-58.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&size=2048x2048"))
