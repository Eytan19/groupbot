import requests
import datetime
import unicodecsv
import json
import csv
from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))

URL = 'https://api.groupme.com/v3/bots/post'
BOT_ID = '0aafafce1aef34384b7bb45233'
HEADERS = {'content-type': 'application/json'}

BDAYS_INPUT = 'bdays.csv'

def bdays(bdays_input, today):
    todays_bdays = []
    with open(bdays_input) as bdays_file:
        bday_data = csv.reader(bdays_file, delimiter=',')
        first_row = next(bday_data)  # skips first Header row
        for row in bday_data:
            bday = row[2]
            bday = bday.split('/')
            month = bday[0]
            day = bday[1]
            if int(month) == today.month and int(day) == today.day:
                todays_bdays.append(row)

    for todays_bday in todays_bdays:
        first_name, last_name = todays_bday['First Name'], todays_bday['Last Name']
        data = {
            'bot_id': BOT_ID,
            'text': 'Happy birthday @{} {}!!!'.format(first_name, last_name)
        }
        response = requests.post(URL, data=json.dumps(data), headers=HEADERS)
        print(response.content)


def main():
    today = datetime.datetime.now()
    bdays(BDAYS_INPUT, today)


if __name__ == '__main__':
    main()
