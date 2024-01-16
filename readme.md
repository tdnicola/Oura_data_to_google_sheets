# Oura to Google Sheets to Day One Integration

I wanted a way to track Oura data on the Day One journal app. 
This Python script is designed to fetch today's Oura data, insert it into a Google Sheets spreadsheet.
Which is then connected with an IFTTT applet to seamlessly import the data into the Day One journal app.


## Data Requested

The python script is only requesting today's readiness and sleep score. 
We will use [gpread](https://docs.gspread.org/en/v5.12.1/) to place the data in a googlesheet.
The 3 data points that are requested are: date, readiness, sleep


## Prerequisites

Before using the script, make sure you have the following:

1. **[Oura API Access Token](https://cloud.ouraring.com/docs/):**
   - Obtain your Oura API access token from the Oura developer platform.

2. **[Google Sheets API Key](https://docs.gspread.org/en/v5.12.1/oauth2.html):**
   - Create an API key in the Google Cloud Console.
   - Share your Google Sheets document with the associated email.
   - Place JSON file in gspread folder

4. **[IFTTT Account](https://ifttt.com/):** 
   - Sign up for an IFTTT account
   - Create an applet:
     - Triggered when a new record is inserted into a google sheet.
     - Day One journal entries when a new row is added to your Google Sheets.

## Installation

1. Install the required Python libraries:

   ```bash
   pip install requests gspread
   ```
2. Obtain the Python script from this repository.
3. Replace the placeholder values in the script:
   - spread_sheet_name: title of the document
   - work_sheet_name: name of the worksheet ex: Sheet1
4. Run script main.py