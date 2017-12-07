
import requests
import datetime
import json
import copy
import argparse

GROUPME_URL = 'https://api.groupme.com/v3/bots/post'
BOT_ID = '0aafafce1aef34384b7bb45233'
COIN_URL = 'https://expresso.gsb.columbia.edu/cas/login?service=https%3A%2F%2Fwww8.gsb.columbia.edu%2Fcareer-management%2'
OCR_URL = 'https://gtscandidate.mbafocus.com/Columbia/Candidates/Authenticated/OCR/InterviewFile.aspx/GetDataSetPage'

def ocr(cred, today):

	with requests.session() as s:
		response = s.post(COIN_URL, data=cred)
		print response
		print response.text
		response = s.post(OCR_URL)
		print response
		print response.text

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--u')
	parser.add_argument('--p')
	args = parser.parse_args()

	cred = {
		'inUserName': args.u,
		'inUserPass': args.p
	}

	today = datetime.datetime.now()
	ocr(cred, today)

if __name__ == '__main__':
	main()