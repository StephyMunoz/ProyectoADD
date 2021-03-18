import pandas as pd
import pymongo 


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.get_database('noticiasbbc')
collection = db.get_collection('AmericaLatina')
df = pd.DataFrame(list(collection.find()))

try:
	df.to_csv('AmericaLatina.csv', index=False)
	print("Saved sucessful ")
except Exception as e:
	raise e
	print("Already exists")
	
