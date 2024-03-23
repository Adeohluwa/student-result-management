import requests
import json
from urllib.parse import urljoin

API_KEY = "AIzaSyCErY0uhX5_jqVhD5xg7FLXj27KUvufyn4"
PROJECT_ID = "babcock-6b68d"
BASE_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:"


def sign_up(email, password):
    url = urljoin(BASE_URL, "signUp?key={}".format(API_KEY))
    data = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()["error"]["message"])


def sign_in(email, password):
    url = BASE_URL + "signInWithPassword?key={}".format(API_KEY)
    data = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })
    headers = {"Content-Type": "application/json"}

    print("URL:", url)
    print("Data:", data)
    print("Headers:", headers)

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()["error"]["message"])

