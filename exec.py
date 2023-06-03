import requests
import pyautogui

while True:
    sc = pyautogui.screenshot('check.jpg')
    url = 'http://26.111.213.113:8000/api/v1/recebedors/'
    '''test = requests.get(url)
    csrftoken = test.cookies.get_dict()
    print(csrftoken)'''
    files = {'img': open('check.jpg', 'rb')}
    send_req = requests.post(url, files=files)
    print(send_req.text)