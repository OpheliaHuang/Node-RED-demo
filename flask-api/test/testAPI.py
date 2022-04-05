from random import randint
import requests
import json
from datetime import date, timedelta, datetime
import traceback
from dateutil import parser


class TestAPI:
    '''This Class lets you test the Flask News API'''
    
    
    def __init__(self, url = "http://0.0.0.0:5000"):
        
        self.url = url
        
    def _get_status(self):

        try:                                                                                                                                                                                                                                                                                                                                                                          
            r = requests.get(self.url)
            return r.status_code

        except Exception as e:
            print(e)
            print(traceback.print_exc()) 

    def _get_data(self, url):

        try:                                                                                                                                                                                                                                                                                                                                                                          
            r = requests.get(url)
            return r.text

        except Exception as e:
            print(e)
            print(traceback.print_exc())  
    
    def test_get(self):

        print("I will now make the specified request")
        try:
            response = self._get_data(self.url + "/all")
            res_dict = json.loads(response)
            date = parser.parse(res_dict["articles"][0]["published"] )
            return date

        except Exception as e:
            print(e)
    
    

if __name__ == "__main__":

    bla_get = TestAPI()
    response = bla_get.test_get()
    print(response)
