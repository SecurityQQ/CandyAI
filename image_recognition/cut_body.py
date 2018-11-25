from PIL import Image
from datetime import datetime
import face_recognition


def get_body(img):
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(image)
    if (face_locations is None) or (len(face_locations) < 1):
        return
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(image)

    top, right, bottom, left = face_locations[0]
    pil_image = Image.fromarray(image)
    nx, ny = pil_image.size

    head_size = right - left

    # print(head_size, left - 2 * head_size, right + 2 * head_size)

    a = 0
    b = nx

    if left - 2 * head_size > 0:
        a = left - 2 * head_size
    if right + 2 * head_size < nx:
        b = right + 2 * head_size
    


    if bottom<0:
        bottom=1;

    face_image = image[bottom:ny, a:b]

    pl_image = Image.fromarray(face_image)
    filename = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + ".png"
    pl_image.save(filename, dpi=(1, 1))
    return filename