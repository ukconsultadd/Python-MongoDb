import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# find_one() returns the first occurence in the selection
x = mycol.find_one()
print(x)
x = mycol.find_one()
print(x)