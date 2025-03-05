import requests
import urllib.parse
from config import apikeys as cfg

target_url = "https://en.wikipedia.org/wiki/Main_Page"


apikey = cfg['htmltopdfkey']   
#print (api_key)

api_url = "https://api.html2pdf.app/v1/generate"

params = {'html': target_url,'apiKey': apikey}
parsed_params = urllib.parse.urlencode(params)
print(parsed_params)

request_url = api_url + "?" + parsed_params
print(request_url)

response = requests.get(request_url)
print(response.status_code)
print(response.text)  # Print error details


result = response.content
with open ("document.pdf", "wb") as handler:
    handler.write(result)
    print("File saved")
