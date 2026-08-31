import pymongo

myclient = pymongo.MongoClient("mongodb+srv://aboodbarghouti4:T7i9A8rCGAOF5iWS@cluster0.ww6rd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Create
mydict = {"name": "John", "address": "Highway 37"}
x = mycol.insert_one(mydict)

# Read
for x in mycol.find():
    print(x)

# Update
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)

# Delete
myquery = {"name": "John"}
mycol.delete_one(myquery)