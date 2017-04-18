import argparse
import csv
import pprint
import requests
import signal
import sys
import json

#API calls here

api_key = 'f9689432b9ef3e61b1c11bcd77d56c145f99e37b' # <--- add your API key here
baseurl = 'https://dashboard.meraki.com/api/v0/'
orgurl = 'https://dashboard.meraki.com/api/v0/organizations/'
headers = {'X-Cisco-Meraki-API-Key': api_key,'Content-Type': 'application/json'}

orgsjson = requests.get(orgurl, headers=headers)

print(orgsjson)
output = json.loads(orgsjson.text)
print(output)




