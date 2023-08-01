import datetime
import requests
import os

# Config Data
USERNAME = 'johnivanpuayap'
USER_TOKEN = os.environ['PIXELA_TOKEN']
GRAPH_ID = 'codingtracker'

# Data
DATE_TODAY = datetime.datetime.now().strftime("%Y%m%d")

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
UPDATE_ENDPOINT = f"{POST_ENDPOINT}/{DATE_TODAY}"
DELETE_ENDPOINT = UPDATE_ENDPOINT

headers = {
    "X-USER-TOKEN": USER_TOKEN
}


def create_user():
    create_user_parameters = {
        "token": USER_TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=create_user_parameters)
    print(response.text)


def create_graph():
    graph_parameters = {
        "id": GRAPH_ID,
        "name": "Coding Hours Tracker",
        "unit": "hours",
        "type": "float",
        "color": "sora",
        "timezone": "Asia/Manila"
    }

    response = requests.post(url=GRAPH_ENDPOINT, headers=headers, json=graph_parameters)
    print(response.text)


def post_pixel(minutes):
    # Post a Pixel in a Graph
    hours = minutes/60
    post_parameters = {
        "date": DATE_TODAY,
        "quantity": f"{hours}",
    }

    response = requests.post(url=POST_ENDPOINT, headers=headers, json=post_parameters)

    if response.json()['isSuccess']:
        print(f"Added{hours: .2f} hours today")


def update_pixel(minutes):
    update_parameters = {
        "quantity": f"{minutes}"
    }

    response = requests.put(url=UPDATE_ENDPOINT, headers=headers, json=update_parameters)
    print(response.text)


def delete_pixel():
    response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
    print(response.text)


print(f"Welcome, {USERNAME}")
mins = int(input("How many minutes did you code today?: "))
post_pixel(mins)
