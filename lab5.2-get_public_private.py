import requests
import json
from config2 import config as cfg

#filename = "repos-public.json"
#filename = "wsaa-code1.json"
filename = "repos-private.json"

#url = 'https://api.github.com/users/filipekojak88/repos?per_page=100'
#url = 'https://api.github.com/repos/filipekojak88/WSAA-assignments/contents'
url = 'https://api.github.com/repos/filipekojak88/aprivateone'


apikey = cfg['privatekey']

#response = requests.get(url)  
response = requests.get(url, auth = ('token', apikey))
print (response.status_code)
repo_json = response.json()


with open(filename, 'w') as fp:
    json.dump(repo_json, fp, indent=4)
