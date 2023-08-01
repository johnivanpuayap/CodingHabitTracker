import datetime

import requests
import os

# Data
USERNAME = 'johnivanpuayap'
USER_TOKEN = os.environ['PIXELA_TOKEN']
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

create_user_parameters = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Create a User
# response = requests.post(url=PIXELA_ENDPOINT, json=create_user_parameters)
# print(response.text)

# Create a Graph Definition

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Coding Hours Tracker",
    "unit": "hour",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

response = requests.post(url=GRAPH_ENDPOINT, headers=headers, json=graph_parameters)
print(response.text)

