import requests
import pyautogui

username = input(str("User: " ))
password = input(str("Pass: " ))
url = 'http://26.111.213.113:8000/api/v1/recebedors/'
auth = (username, password)
while True:
    sc = pyautogui.screenshot('check.jpg')
    files = {'img': open('check.jpg', 'rb')}
    send_req = requests.post(url, files=files, auth=auth)
    print(send_req.content)
    if send_req.status_code != 200:
        break