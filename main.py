import requests
import os

# DATA
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USER_TOKEN = os.environ['PIXELA_TOKEN']

create_user_parameters = {
    "token": USER_TOKEN,
    "username": "johnivanpuayap",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # CREATE A USER
# response = requests.post(url=PIXELA_ENDPOINT, json=create_user_parameters)

