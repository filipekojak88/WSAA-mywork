import requests
import urllib.parse
from config import config as cfg

target_url = "https://en.wikipedia.org"


api_key = cfg['htmltopdfkey']   

api_url = "https://api.html2pdf.app/v1/generate"

params = {
    'html': target_url,
    'apikey': api_key
}
parsed_params = urllib.parse.urlencode(params)
print(parsed_params)
request_url = api_url + "?" + parsed_params
print(request_url)

response = requests.get(request_url)
print(response.status_code)
print(response.text)  # Print error details


result = response.content
with open ("document.pdf", "wb") as f:
    f.write(result)
    print("File saved")
