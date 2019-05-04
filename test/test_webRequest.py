# testing / mytest.py

from app.webRequest import enlarge
from app.webRequest import returnCity

#Adapted from in class exercise to set up automated testing
def test_enlarge(): 
    result = enlarge(3) 
    assert result == 300 

#Test if the package returns desired city
def test_returnCity():
    result = returnCity(11355)
    assert result == "FLUSHING"