import requests
import bs4
import os
from dotenv import load_dotenv

URL = 'https://services.surfline.com/trusted/token?isShortLived=false'
# signin = 'https://www.surfline.com/sign-in'
load_dotenv()
user = os.getenv('SURFLINE_USERNAME')
password = os.getenv('SURFLINE_PASSWORD')
print(user)

s = requests.Session()

login = {
    'grant_type': 'password',
    'username': user,
    'password': password,
#     'device_id': 'Chrome-113.0.0.0',
#     'device_type': 'Chrome 113.0.0.0 on OS X 10.15.7 64-bit',
#     'forced': True
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}

response = s.post(URL, data=login, headers=headers)
