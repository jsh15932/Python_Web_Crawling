import os
import sys
import requests
import json

client_id = "c4PFSQ9Y6r1jMy0q298Z"
client_secret = "5JRNB7pTHf"
url = "https://openapi.naver.com/v1/vision/face"
files = {'image': open('디카1.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url, files=files, headers=headers)
rescode = response.status_code
if(rescode == 200):
    data = json.loads(response.text)
    faceCount = data['info']['faceCount']
    print("감지된 얼굴 수는 {}입니다.".format(faceCount))
else:
    print("Error Code:" + rescode)