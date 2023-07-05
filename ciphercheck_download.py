#!/usr/bin/python3
# Downloads latest cipher suites (including "weak" etc rating) from ciphersuite.info API 
# To copy into a file just run $ ciphercheck_download.py > db.json
#
# # # # # # # # # #


import requests
import json

def get_all_ciphersuites():
	base_url = 'https://ciphersuite.info/api'
	endpoint = '/cs'
	url = f'{base_url}{endpoint}'
	response = requests.get(url)
	response.raise_for_status()
	data = response.json()
	print(json.dumps(data, indent=4))

get_all_ciphersuites()
