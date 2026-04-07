def hash_password(password, salt):
    salted_password = password + salt
    return hash(salted_password)

import os

def generate_dynamic_salt():
    return os.urandom(16).hex()

def register_user(username, password, user_db):
    salt = generate_dynamic_salt()
    hashed_password = hash_password(password, salt)
    user_db[username] = (hashed_password, salt)
    
def authenticate_user(username, password, user_db):
    if username not in user_db:
        return False
    hashed_password, salt = user_db[username]
    return hash_password(password, salt) == hashed_password

user_db = {}
register_user("user1", "password1", user_db)
register_user("user2", "password2", user_db)
register_user("user3", "password3", user_db)
register_user("user4", "password4", user_db)
register_user("user5", "password5", user_db)

print(authenticate_user("user1", "password1", user_db))
print(authenticate_user("user2", "wrong_password", user_db))

print(authenticate_user(input("Login:"), input("Password:"), user_db))