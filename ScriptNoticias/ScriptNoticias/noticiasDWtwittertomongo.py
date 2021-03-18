
from twython import TwythonStreamer
from pymongo import MongoClient


###API ########################

ckey='Bg7OF6fQ17rLsvDZgk2SenEK'
csecret ='c55CrtVrzTBtDcO58I2GpEp2xB3u8EV4b77npFyKJSd4oRaFO'
atoken = '1339680483458904068-TLFBtZElCFTtw4e9HRCQlLNtLBMqK1'
asecret = 'B90yDCNoPWgIP2qkmrfqfLMk6qXH1mc9HjNQduGrqIMa'

###API ########################

db = MongoClient('mongodb://localhost:27017').noticiasdwesp

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        print(data)
        db.dw4.insert(data)

        def on_error(self, status):
            print(status)
            
stream = MyStreamer(ckey, csecret,
                    atoken, asecret)

stream.statuses.filter(track = 'dw_espanol')




