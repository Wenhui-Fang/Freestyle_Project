# testing / mytest.py

from app.webRequest import enlarge

def test_enlarge(): # note the function name is prefixed with "test_"
    result = enlarge(3) # directly invoke the function we want to test
    assert result == 300 # describe expectations for desired behavior