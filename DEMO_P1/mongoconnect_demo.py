########MONGO CONNECTION STRING


from pymongo import MongoClient

client = MongoClient()

db = client.ESCAPE_ROOM

collection = db.file_saves