# testing / mytest.py

from app.webRequest import enlarge
from app.webRequest import returnCity
from app.webRequest import returnState

#Adapted from in class exercise to set up automated testing
def test_enlarge(): 
    result = enlarge(3) 
    assert result == 300 

#Test if the zipcode package returns desired city
def test_returnCity():
    result = returnCity(11355)
    assert result == "FLUSHING"
#Test if the uszipcode package returns desired state
def test_returnState():
    result = returnState(20057)
    assert result == "DC"