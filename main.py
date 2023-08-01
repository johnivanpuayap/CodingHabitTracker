import datetime
import requests
import os

# Change this when you want to add new data (can be in minutes)
NO_OF_MINUTES = 200

# Data
USERNAME = 'johnivanpuayap'
USER_TOKEN = os.environ['PIXELA_TOKEN']
DATE_TODAY = datetime.datetime.now().strftime("%Y%m%d")
GRAPH_ID = ''

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
UPDATE_ENDPOINT = f"{POST_ENDPOINT}/{DATE_TODAY}"

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

# response = requests.post(url=GRAPH_ENDPOINT, headers=headers, json=graph_parameters)
# print(response.text)

# # Post a Pixel in a Graph

#
# post_parameters = {
#     "date": DATE_TODAY,
#     "quantity": f"{NO_OF_MINUTES/60}",
# }
#
# response = requests.post(url=POST_ENDPOINT, headers=headers, json=post_parameters)
# print(response.text)

# Update a Pixel
#
#
# update_parameters = {
#     "quantity": f"{NO_OF_MINUTES/60}"
# }
#
# response = requests.put(url=UPDATE_ENDPOINT, headers=headers, json=update_parameters)
