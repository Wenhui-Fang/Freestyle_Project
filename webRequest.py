import requests
import xml.etree.ElementTree as ET
# import xmltodict
from bs4 import BeautifulSoup


request_url = ("https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz17zh9n8ivpn_7j3qs&state=wa&city=seattle&childtype=neighborhood")
response = requests.get(request_url)
print(response)
print(type(response))
contents = response.text
print(type(contents))

soup = BeautifulSoup(contents,'xml')

# print(soup)
print(type(soup))

# breakpoint()

# soup.find("response").find_all("list")
# Response_list = soup.find("response").find("list")
# price = soup.find("response").find("list").find("region").find_all("zindex")



regions = soup.find("response").find("list").find_all("region")

for i in range(0,len(regions)):
    # print(regions[i].find("zindex").text)
    price = regions[i].find("zindex")
    if price:
        print(price.text)
    else:
        print("No price available for this region.")



# http://www2.hawaii.edu/~takebaya/cent110/xml_parse/xml_parse.html
# from bs4 import BeautifulSoup
# infile = open("books.xml","r")
# contents = infile.read()
# soup = BeautifulSoup(contents,'xml')
# titles = soup.find_all('title')
# authors = soup.find_all('author')
# prices = soup.find_all('price')
# for i in range(0, len(titles)):
#     print(titles[i].get_text(),"by",end=' ')
#     print(authors[i].get_text(),end=' ')
#     print("costs $" + prices[i].get_text())


# for i < len(price):
#     Price_list.append(price[0].text)






# zillow_api = "https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz17zh9n8ivpn_7j3qs&state=wa&city=seattle&childtype=neighborhood"

# try:
#     r = requests.head(zillow_api)
#     print(r.status_code)

#     if (r.status_code) == 200:
#         print(type(r))
#         print(r)

#         # where do I specify xml or json?

#     # prints the int of the status code. Find more at httpstatusrappers.com :)
# except requests.ConnectionError:
#     print("failed to connect")



# import numpy as np
# import json
# import os
# import requests

# # api_key = os.environ.get("ALPHAVANTAGE_API_KEY")


#   # making a request after successful data validation
# request_url = ('http://api.indeed.com/ads/apisearch?publisher=123412341234123&q=java+developer&l=austin%2C+tx&sort=&radius=&st=&jt=&start=&limit=&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2')
# response = requests.get(request_url)

# # type(response)

# # parsed_response = json.loads(response.text)

# # print(parsed_response)
# # type(parsed_response)