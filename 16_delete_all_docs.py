import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Delete all documents in the "customers" collection:
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")