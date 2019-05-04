# testing / mytest.py

from app.webRequest import enlarge
from app.webRequest import returnCity

def test_enlarge(): # note the function name is prefixed with "test_"
    result = enlarge(3) # directly invoke the function we want to test
    assert result == 300 # describe expectations for desired behavior

def test_returnCity():
    result = returnCity(11355)
    assert result == "FLUSHING"