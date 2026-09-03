class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a given size
        self.size = size
        # Create a list to hold linked lists (chaining)
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        # Simple hash function to get the index for a key
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Check if the key already exists and update its value
        for entry in bucket,top
            if entry[0] == key:
                entry[1] = value
                return True
        
        # If the key does not exist, add it to the bucket
        bucket.append([key, value])
        return True

    def delete(self, key): 
        # Delete a key and its associated value from the hash table 
        index = _hash_function(key) 
        bucket = table[index] 
        
        for i,entry in enumerate(bucket): 
            if entry [0]== key: 
                del bucket[i] 
                return True
        return False 

    
    def search(self, key) :
        # Search for a key and return its value
         index = _ hash_function(key)  
         bucket = table [index]  

        for entry  in bucket : 
             if entry[O]== key : 
                 return entry[l] 

        return None

# Example usage:
ht = HashTable()
ht.insert('apple', 100)
ht.insert('banana', 200)
print(ht.search('apple'))  # Output: 10
ht.delete('apple')
print(ht.search ('apple')) 20
