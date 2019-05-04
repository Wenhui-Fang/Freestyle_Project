# Tell Me Where To Live

Tell-Me-Where-To-Live is an application that helps housing seekers conduct preliminary research by searching all neighborhoods that meet their commute needs (e.g. the distance from their target location based on zipcode). It returns the list of neighborhoods housing seekers could potentially consider, as well as all the housing listings in these neighborhoods classified by price range. The application allows housing seekers to learn the affordability of the neighborhoods in a few seconds so they can plan forward.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

# Prerequisites
1. Anaconda 3.7
2. Python 3.7
3. Pip
4. uszipcode: 
  <br />Install:
  <br />$ pip install uszipcode
  <br />To upgrade to latest version:
  <br />$ pip install --upgrade uszipcode
  <br />For further exploration, see documentation 
  <br />https://pypi.org/project/uszipcode/
5. PySimpleGUI: 
  <br />Install:
  <br />$ pip install PySimpleGUI
  <br />For further exploration, see documentation 
  <br />https://pypi.org/project/PySimpleGUI/

6. zipcodes: 
  <br />Install
  <br />$ pip install zipcodes
  <br />For further exploration, see documentation 
  <br />https://pypi.org/project/zipcodes/
  
# Installation
A step by step series of examples that tell you how to get a local copy of application running

When you install Python, you also get Python's package manager, pip. You can use pip to install and manage third-party Python packages.
For this Project, first create and activate a new Anaconda virtual environment, perhaps named "tell-me-where-to-live-env":

conda create -n tell-me-where-to-live-env
<br />conda activate tell-me-where-to-live-env

Then install package dependencies by specifying the requirements:
<br />pip install -r requirements.txt

Then navigate to your local root path and execute the script by running the command below:
<br />python app/webRequest.py 

# Envrionment Setting
This project requires only a gitignore to ensure caches (__pycache__. and pytest_cache) caused by automated testings will not interupt the execution of the program. No other envrionment setting is currently needed as this code retrieves data using a third party package, not API keys.

# Security Setting
As mentioned above, no confidential information will be used so security setting is unnecessary. 

# Running the tests
To run automated tests, consider installing pytest using pip:
<br />$ pip install pytest
<br />The pytest package is generally used as a command-line utility for running pre-defined files of "test" code.
Navigate to the local root path, and invoke pytest using the command below:
<br />pytest #> 1 passed in 0.01 seconds

# Deployment
As this application contains a graphica user interface created by PySimpleGUI, using local envrionment is recommended. Further exploration needs to be done for online deployment.

# Author
Wenhui Fang, a senior at Georgetown University and a python beginner 

# License
This project is licensed under the MIT License - see the LICENSE.md file for details

# Acknowledgments
This project is inspired by Prof. Michael Rossetti, who teaches OPIM 244 - Managing Business Application in Python at Georgetown University. Here is a link to his github: https://github.com/prof-rossetti. In addition, I have adopted my GUI from https://pypi.org/project/PySimpleGUI/
