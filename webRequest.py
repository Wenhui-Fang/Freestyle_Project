
import numpy as np
import json
import os
import requests

# api_key = os.environ.get("ALPHAVANTAGE_API_KEY")


  # making a request after successful data validation
request_url = ('http://api.indeed.com/ads/apisearch?publisher=123412341234123&q=java+developer&l=austin%2C+tx&sort=&radius=&st=&jt=&start=&limit=&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2')
response = requests.get(request_url)

type(response)

parsed_response = json.loads(response.text)

print(parsed_response)
type(parsed_response)