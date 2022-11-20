# yes, this is prob slower than some other alternative but im lazy :)

import requests, cv2, os

URL = "https://thispersondoesnotexist.com/image"
HEADERS = {'User-Agent': 'Mozilla FireFox 3.0'}

def download_face():
    with open(f"{path}/temp/temp_img.jpg", 'wb') as write_face:
        write_face.write(requests.get(URL, headers=HEADERS).content)
        face = cv2.imread("temp/temp_img.jpg")
        return face

        # image = cv2.resize(face, (150, 150))
        # cv2.imshow("Face", face)
        # cv2.waitKey(300)
