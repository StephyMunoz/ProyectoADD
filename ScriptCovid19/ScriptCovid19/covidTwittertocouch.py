import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#-------------------------------------------#
ckey='Bg7OF6fQ17rLsvDZgk2SenEK'
csecret ='c55CrtVrzTBtDcO58I2GpEp2xB3u8EV4b77npFyKJSd4oRaFO'
atoken = '1339680483458904068-TLFBtZElCFTtw4e9HRCQlLNtLBMqK1'
asecret = 'B90yDCNoPWgIP2qkmrfqfLMk6qXH1mc9HjNQduGrqIMa'

#-------------------------------------------#
class listener(StreamListener):
    
    def on_data(self, data):
        dataTweet = json.loads(data)
        try:
            
            dataTweet["_id"] = str(dataTweet['id'])
            doc = db.save(dataTweet)
            print ("Saved sucessful" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
#-------------------------------------------# 

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#-------------------------------------------#

server = couchdb.Server('http://admin:12345@localhost:5984/') 
try:
    db = server.create('covidrec6')
except:
    db = server['covidrec6']
    
#-------------------------------------------#

twitterStream.filter(track=['covid19'])
