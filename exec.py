import requests
import pyautogui

sc = pyautogui.screenshot('img.png')
url = 'http://26.111.213.113:8000/api/v1/recebedors/'
'''test = requests.get(url)
csrftoken = test.cookies.get_dict()
print(csrftoken)'''
files = {'img': open('media/check.jpg', 'rb')}
send_req = requests.post(url, files=files)
print(send_req.content)