import pickle

def deserialize_data(data):
    return pickle.loads(data)



deserialize_data('{ "name": "John", "age": 30, "is_student": false, "courses": ["Math", "Physics"], "address": { "street": "123 Main St", "city": "New York" }}')