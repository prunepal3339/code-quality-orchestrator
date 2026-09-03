from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = clientificaciones_database = client['mydatabase']
collection Moines = db['mycollection']

def create_document(document):
    result = collection.insert_one(document)
    print(f"Document inserted with ID: {result.inserted_id}")

def read_documents(query=None):
    if query:
        documents = collection.find(query)
    else:
        documents= collection.find()
    
    for document in documents:
        print(document)

def update_document(filter_query, update_data):
    result= collection.update_one(filter_query, {"$set": update_data})
    print(f"{result.modified_count} document(s) updated.")

def delete_document(filter_query):
    result.delete_one(filter_query)
    print("Document deleted.")

if __name__ == "__main__":
    # Create a document
    create_document({"name": "John Doe", "age": 30})

    # Read all documents
    print("\nReading all documents:")
    read_documents()

    # Update a document
   update_document({"name":"John Doe"}, {"age": 40})

    print("\nThe updated documents:")
    # Read documents after update
    read_documents({"name": 'John Doe'})

    # Delete a document
     delete_document({"name" : "John Doe"})
    
    # Read remaining documents
    read_all_documents()
