from django.test import TestCase
import requests
# Create your tests here.


class Testcases():


    def _check_login(self,):
        url = "http://127.0.0.1:8080/login"
        data = {"username":"windows","password":"Wind0ws@88"}
        r = requests.post(url,data=data)
        print(r.text)

    def check_location(self):
        url="http://127.0.0.1:8080/api/v1/location/"
        headers = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6IndpbmRvd3MiLCJleHAiOjE1NDQ1MTUwMTgsImVtYWlsIjoiIn0.JHxcA3tRlKKqxoypmN5n3JpPZu1a4Gb3yAnixh_RaVM"}
        r= requests.get(url,headers = headers)
        print(r.text)


test=Testcases()
##test.check_login()
test.check_location()
    
