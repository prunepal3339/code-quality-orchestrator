from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Select the database
db = client["mydatabase"]

# Select or create a collection
collection = db["customers"]

def create_record():
    name = input("Enter customer name: ")
    email = input("Please enter customer email: ")

    # Create a dictionary containing customer data
    customer_data = {"name": name, "email": email}

∀
