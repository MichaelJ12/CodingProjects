class HashTable:
    def __init__(self, capacity=11):
        self.capacity = capacity # total number of slots (buckets)
        self.size = 0 # number of key value pairs
        self.table = [[] for _ in range(capacity)] # list of empty lists (chaining)

    def _hash_function(self,key):
        # generatge an index based on the key 
        return hash(key) % self.capacity 
    
    def insert(self, key, value):
        # insert a key-value pair into the table
        index = self._hash_function(key)
        bucket = self.table[index]

         # check if a key already exist
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value # upadte the existing key
                return
            
        # if the key doesnt exist, append new pair
        bucket.append([key, value])
        self.size += 1

    def get(self, key):
        # retrieve the value associated with the key
        index = self._hash_function(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1] # return the value
            
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        # remove key-value pair form the hash table
        index = self._hash_function(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                self.size -= 1 
                return pair

        raise KeyError(f"Key '{key}' not found")

    def size_t(self):
        # return the number of elemetns in the hash table
        return self.size
    
    def items(self):
        # return a list of all key-value pairs in the hash table
        return [(pair[0], pair[1]) for bucket in self.table for pair in bucket]
    
    def _resize(self):
        # double the table size and rehash all elements.
        new_capacity =  self.capacity * 2 
        new_table = [[] for _ in range(new_capacity)]

        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_capacity
                new_table[new_index].append([key, value])

        self.capacity = new_capacity
        self.table = new_table 

if __name__ == '__main__':
    h_table = HashTable()


    h_table.insert("name", "alice")
    h_table.insert("age", 20)
    h_table.insert("hight", "190cm")
    h_table.insert("hobby", "drawing")
    h_table.insert("coolmeter", 99999)
    h_table.insert("cookie", 2)
    h_table.insert("hair", 'semi-afro;')
    h_table.insert("idk", 'semi-2;')
    h_table.insert("test", 'tesst;')
    h_table.insert("drawing", 'ninja')
    h_table.insert("1", '1')


    print(h_table.get("hair"))

    print(h_table.size_t())

    print(h_table.items())