import requests
from datetime import date
from datetime import timedelta
from googleSheets import insert_Oura_Scores
import json
with open('credentials.json', 'r') as f:
        config = json.load(f)

access_token = config['oura']['access_token']

today = date.today()
yesterday = today - timedelta(days = 1)

# Replace 'YOUR_ACCESS_TOKEN' with your actual Oura API access token

# Define the API endpoints for fetching sleep and readiness data
sleep_endpoint = 'https://api.ouraring.com/v1/sleep'
readiness_endpoint = 'https://api.ouraring.com/v1/readiness'

sleepScore = ''
readinessScore = ''

# Set up the headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

def get_sleep_data(start_date, end_date):
    # Set up the parameters for the sleep request
    params = {
        'start': start_date,
        'end': end_date
    }

    # Make the sleep request to the Oura API
    response = requests.get(sleep_endpoint, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        sleep_data = response.json()
        try:
            sleep_Score = sleep_data['sleep'][0]['score']
            return sleep_Score
        except:
            print(f'No sleep score data for today: {today}')
    else:
        print(f"Error fetching sleep data: {response.status_code}")
        return None

def get_readiness_data(start_date, end_date):
    # Set up the parameters for the readiness request
    params = {
        'start': start_date,
        'end': end_date
    }

    # Make the readiness request to the Oura API
    response = requests.get(readiness_endpoint, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        readiness_data = response.json()
        try:
            readiness_Score = readiness_data['readiness'][0]['score']
            return readiness_Score
        except:
             print(f'No ReadyScore data for today: {today}')
        return readiness_data
    else:
        print(f"Error fetching readiness data: {response.status_code}")
        return None

# Fetch sleep data
sleep_data = get_sleep_data(yesterday,today)
# Fetch readiness data
readiness_data = get_readiness_data(yesterday, today)

#Change today into a string instead of a date object
today = today.strftime('%Y-%m-%d')

insert_Oura_Scores(today, readiness_data, sleep_data)
