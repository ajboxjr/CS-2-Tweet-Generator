import requests
import sys
import random
import json

app_id= "9032a5bf"

app_key = "c3deb04a72619c5adbbc8401dcf95336"

language = 'en'


url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + sys.argv[1]


r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
