import pymongo

# creating the MongoClient object
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# creating the database named "mydatabase"
mydb = myclient["mydatabase"]

dblist = myclient.list_database_names()

if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("this db does not exist ")