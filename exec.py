import requests
import pyautogui

sc = pyautogui.screenshot('img.png')
url = 'http://127.0.0.1:8000/api/v1/recebedors/'
'''test = requests.get(url)
csrftoken = test.cookies.get_dict()
print(csrftoken)'''
files = {'img': open('media/ark.png', 'rb')}
send_req = requests.post(url, files=files)
print(send_req.content)