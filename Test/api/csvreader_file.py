import csv
import json

from urllib.request import urlopen,build_opener,install_opener,Request



class Csvtomongo:

    def __init__(self, path):
        self.path = path


    def readcsv(self):
        self.rows=[]
        host = "127.0.0.1:8000"
        with open(self.path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                url = 'http://'+host+'/api/v1/'#'http://' + host +'/act/api/'
                data = json.dumps(dict(i)).encode('utf-8')
                req = Request(url,data,{'Content-Type': 'application/json'})
                resp = urlopen(req)
                contents = resp.read()
                res = contents.decode('utf-8')
                print(res)




csvdump = Csvtomongo("C:\\Users\\vvadla\\Downloads\\imar_technolgy_test\\Full Stack-Data.csv")
csvdump.readcsv()
