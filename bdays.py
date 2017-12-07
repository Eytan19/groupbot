
import requests
import datetime
import unicodecsv
import json

URL = 'https://api.groupme.com/v3/bots/post'
BOT_ID = '0aafafce1aef34384b7bb45233'
HEADERS = {'content-type': 'application/json'}

BDAYS_INPUT = '/Users/eytan/groupbot/bdays.csv'

def bdays(bdays_input, today):

	todays_bdays = []
	with open(bdays_input, 'rU') as bday_file:
		bday_data = unicodecsv.DictReader(bday_file, encoding='utf-8-sig')
		for row in bday_data:
			bday = row['Birthday']
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
		print response.content
	

def main():

	today = datetime.datetime.now()
	bdays(BDAYS_INPUT, today)

if __name__ == '__main__':
	main()


