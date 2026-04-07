hash_table = [None] * 20

def hash_function(key):
    return len(key) % 20

def add_to_hash_table(hash_table, key, value):
    index = hash_function(key)
    while hash_table[index] is not None:
        if hash_table[index][0] == key:
            hash_table[index] = (key, value)
            return
        index = (index + 1) % len(hash_table)
    hash_table[index] = (key, value)
    
def get_from_hash_table(hash_table, key):
    index = hash_function(key)
    while hash_table[index] is not None:
        if hash_table[index][0] == key:
            return hash_table[index][1]
        index = (index + 1) % len(hash_table)
    return None

products = {
    "Apple": 1.0,
    "Banana": 0.5,
    "Orange": 0.8,
    "Grapes": 2.0,
    "Mango": 1.5,
    "Pineapple": 3.0,
    "Strawberry": 0.2,
    "Blueberry": 0.3,
    "Watermelon": 4.0,
}

for product, price in products.items():
    add_to_hash_table(hash_table, product, price)
    
print(hash_table)

load_factor = sum(1 for item in hash_table if item is not None) / len(hash_table)
print(f"Load factor: {load_factor:.2f}")

for i in products.keys():
    print(f"{i} <-> {get_from_hash_table(hash_table, i)}")
    print(products[i] == get_from_hash_table(hash_table, i))