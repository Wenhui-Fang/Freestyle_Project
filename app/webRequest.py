from uszipcode import SearchEngine
from uszipcode import Zipcode
import PySimpleGUI as sg  
import sys
import zipcodes


def enlarge(i):
    return i * 100

if __name__ == "__main__":

        #Simpe GUI adapted from https://pypi.org/project/PySimpleGUI/, allowing the users to set their preferences
        layout = [[sg.Text('Welcome to use Tell-Me-Where-To-Live', size=(30, 1), font=("Helvetica", 25), text_color='blue')],      
        [sg.Text('Please enter the zip code where you will work or go to college')],      
        [sg.Text('zipcode', size=(15, 1)), sg.InputText('20057', key='_zipcode_')],
        [sg.Text('Please determine how many miles you are willing to commute, and your desired room plan.',)],       
        [sg.Checkbox('< 10 miles', size=(10,1)),  sg.Checkbox('10 - 30 miles', default=True)],
        [sg.Radio('I want a studio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('I want 1b1b!', "RADIO1")],      
        [sg.Text('My Monthly Budget is:', size=(18, 1))],    
        [sg.InputCombo(['<= $1,000', '> $1,000'], size=(20, 3))],      
        [sg.Submit(), sg.Cancel()]]    
        event, values  = sg.Window('OPIM 242 FreeStyle Project', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()    

        #Input validation using zipcodes package; terminates the application if wrong input is captured;
        #Sample vlaues captured from user inputs: {'_zipcode_': '20057', 0: True, 1: True, 2: True, 3: False, 4: '<= $1,000'}
        try:
                zipcodes.matching(values['_zipcode_'])
        except: 
                TypeError
                sg.Popup("Warning!","You must enter a right zip code. The application will terminate now. Please start again...")
                sys.exit()

        #Input validation - Miles to commute; terminates the application if no option is selected;
        if values[0] == True and values[1] == False:
                miles_to_commute = 10
        elif values[1] == True and values[0] == False:
                miles_to_commute = 30
        elif values[0] == True and values[0] == True:
                miles_to_commute = 30
        else: 
                sg.Popup("Warning!","You must select miles you are willing to commute. The application will terminate now. Please start again...")
                sys.exit()

        #Read the users' preferred housing;
        if values[2] == True:
                housing_style = "studio"
        elif values[3] == True:
                housing_style = "1b1b"

        #Read the users' budget;
        if values[4] == "<= $1,000":
                budget = "less than $1,000."
        elif values[4] == "> $1,000":
                budget = "more than $1,000."

        #Input Validation complete, start using built-in functions within uszipcode package to request data
        #Refer to https://pypi.org/project/uszipcode/ for more info regarding below functions
        user_zipcode = values['_zipcode_']  
        search = SearchEngine(simple_zipcode=False)
        zipcode = search.by_zipcode(user_zipcode)

        #converting data to dictionary
        matching_zip = zipcode.to_dict()

        #Some zipcodes are associated with PO Boxes which require a different way of presenting the location
        if matching_zip["post_office_city"] != "None":
                matching_city = matching_zip["post_office_city"]
        else:
                matching_city = (matching_zip["county"] + ", " + matching_zip['state'])

        #Let the users know their input with a pop-up window
        sg.Popup('Input Verification',"So you will be studying or working in " + matching_city + ". And you are willing to commute up to " + 
        str(miles_to_commute) + " miles. You want a " + housing_style + " and your budget is " + budget + ". Click Ok to Proceed...")

        #using built-in data within uszipcode package to determine latitude and longtitude of the target zipcode/location
        latitude = matching_zip["lat"]
        longtitude = matching_zip["lng"]

        #using a built-in function within uszipcode package to search nearby neighborhodds, setting maximum 10 neighborhoods for now to shorten search time
        nearby_neighborhoods = search.by_coordinates(latitude, longtitude, radius=int(miles_to_commute),returns=10)

        where_to_live = []
        housing_listing = []

        print("Below is a list of neighborhoods you can consider: \n")
        #search and append the results
        for i in range(0,len(nearby_neighborhoods)):
                city = nearby_neighborhoods[i].post_office_city
                if city not in where_to_live:
                        where_to_live.append(city)
                        if housing_style == "studio":
                                housing_listing.append(nearby_neighborhoods[i].monthly_rent_including_utilities_studio_apt)
                        elif housing_style == "1b1b":
                                housing_listing.append(nearby_neighborhoods[i].monthly_rent_including_utilities_1_b)
                        print(city + "\n")

        # print housing listing
        
        print("Monthly rent including utilities for a " + housing_style + " is as follows: \n")
        print("Price Range: " + "       " + "Number of listings: ")
        print("____________________________________")

        #print housing listings based on 6 price ranges determined by the package;
        for i in range(0, 6):
                print((housing_listing[0][0]["values"][i]["x"]).ljust(10) + ":"+ (str(housing_listing[0][0]["values"][i]["y"]).rjust(25)))

        ############################ For future exploration which is to build a user-friendly output window ##################################
        # breakpoint()
        # breakpoint()
        # print(housing_listing[1][0]["values"][0]["x"])
        # sg.Popup("Below is a list of neighborhoods you can consider:", where_to_live)
        # print=sg.Print  
        # for i in range(0, 6):
        #         sg.Print((housing_listing[0]["values"][i]["x"]).ljust(10) + ":"+ (str(housing_listing[0]["values"][i]["y"]).rjust(25)))

        # #to hold above print list
        # sg.PopupScrolled(print("Price Range: " + "       " + "Number of listings: "))
