hash_table_size = 10
hash_table = [[] for i in range(hash_table_size)]

def add_to_hash_table(hash_table, key, value):
    index = hash(key) % hash_table_size
    if hash_table[index] is None:
        hash_table[index] = [(key, value)]
    else:
        for i, (k, v) in enumerate(hash_table[index]):
            if k == key:
                hash_table[index][i] = (key, value)
                return
        hash_table[index].append((key, value))
        
print(hash_table)

add_to_hash_table(hash_table, "key1", "value1")
add_to_hash_table(hash_table, "key2", "value2")

print(hash_table)