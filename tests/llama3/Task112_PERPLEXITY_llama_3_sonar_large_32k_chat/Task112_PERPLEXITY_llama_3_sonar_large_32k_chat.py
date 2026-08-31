import pymongo

client = pymongo.MongoClient("mongodb+srv://aboodbarghouti4:T7i9A8rCGAOF5iWS@cluster0.ww6rd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
collection = db["mycollection"]

# Create
data = {"name": "John", "age": 30}
collection.insert_one(data)

# Read
data = collection.find_one({"name": "John"})
print(data)

# Update
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# Delete
collection.delete_one({"name": "John"})