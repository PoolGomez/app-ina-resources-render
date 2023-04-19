from pymongo import MongoClient
#from pymongo.server_api import ServerApi

uri = "mongodb+srv://paul479:Villapaul123@cluster0.lkdesur.mongodb.net/?retryWrites=true&w=majority"

#conn = MongoClient(uri, server_api = ServerApi('1'))
conn = MongoClient(uri).cluster0


