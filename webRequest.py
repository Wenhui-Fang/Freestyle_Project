import requests
import xml.etree.ElementTree as ET
# import xmltodict
from bs4 import BeautifulSoup
from uszipcode import SearchEngine
import re
import PySimpleGUI as sg  



#adapted from https://pypi.org/project/PySimpleGUI/

layout = [[sg.Text('All graphic widgets in one window!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],      
   [sg.Text('Here is some text.... and a place to enter text')],      
   [sg.InputText()],      
   [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],      
   [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],      
   [sg.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',)],      
[sg.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),      
 sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],      
[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),      
 sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),      
 sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),      
 sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],      
[sg.Text('_'  * 100, size=(70, 1))],      
[sg.Text('Choose Source and Destination Folders', size=(35, 1))],      
[sg.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Source'),      
 sg.FolderBrowse()],      
[sg.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Dest'),      
 sg.FolderBrowse()],      
[sg.Submit(), sg.Cancel(), sg.Button('Customized', button_color=('white', 'green'))]]      

event, values  = sg.Window('Everything bagel', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()    



user_zipcode = input("Please tell me where you will work / go to college by entering the zip code...")

#using uszipcode package to request data
search = SearchEngine(simple_zipcode=False)
zipcode = search.by_zipcode(user_zipcode)

#converting data to dictionary
matching_zip = zipcode.to_dict()
matching_city = matching_zip["post_office_city"]
matching_state = matching_zip["state"]

print("So you will be studying or working in " + matching_city + ".")

latitude = matching_zip["lat"]
longtitude = matching_zip["lng"]

miles_to_commute = input("How many miles are you willing to commute?")


# nearby_neighborhoods = search.by_coordinates(latitude, longtitude, radius=int(miles_to_commute), returns=5)
nearby_neighborhoods = search.by_coordinates(latitude, longtitude, radius=int(miles_to_commute),returns=10)

where_to_live = []
housing_listing_1b = []
print("Below is a lit of neighborhoods where you can live: ")

for i in range(0,5):
    city = nearby_neighborhoods[i].post_office_city
    if city not in where_to_live:
        where_to_live.append(city)
        housing_listing_1b = nearby_neighborhoods[i].monthly_rent_including_utilities_1_b
        print(city + "\n")

# print(housing_listing)

print("Monthly rent including utilities for 1b is as follows: ")

print("Price Range: " + "       " + "Number of listings: ")

number_of_listing = len(housing_listing_1b)

for i in range(0, 6):
    print(housing_listing_1b[0]["values"][i]["x"] + ":             " + str(housing_listing_1b[0]["values"][i]["y"]))


# city_no_space = re.sub(' ','',matching_city)



# test = nearby_neighborhoods[0]
# test.major_city


# # print(type(zipcode))

# breakpoint()

# # request_url = ("https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz17zh9n8ivpn_7j3qs&state=wa&city=seattle&childtype=neighborhood")
# # request_url = ("https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz17zh9n8ivpn_7j3qs&state=ny&city=newyork&childtype=neighborhood")
# request_url = ("https://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz17zh9n8ivpn_7j3qs&state=ny&city=newyork&childtype=zipcode")

# response = requests.get(request_url)


# print(response)
# print(type(response))
# contents = response.text
# print(type(contents))

# soup = BeautifulSoup(contents,'xml')

# # print(soup)
# print(type(soup))



# soup.find("response").find_all("list")
# Response_list = soup.find("response").find("list")
# price = soup.find("response").find("list").find("region").find_all("zindex")



# regions = soup.find("response").find("list").find_all("region")

# for i in range(0,len(regions)):
#     # print(regions[i].find("zindex").text)
#     price = regions[i].find("zindex")
#     if price:
#         print(price.text)
#     else:
#         print("No price available for this region.")


breakpoint()

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