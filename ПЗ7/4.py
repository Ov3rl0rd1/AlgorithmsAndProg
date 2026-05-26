def hash_password(password, salt):
    salted_password = password + salt
    return hash(salted_password)

static_salt = "static_salt"

import os

def generate_dynamic_salt():
    return os.urandom(16).hex()


password = "my_secure_password"

hashed_password_static = hash_password(password, static_salt)
print(f"Hashed password with static salt: {hashed_password_static}")

hashed_password_static = hash_password(password, static_salt)
print(f"2 Hashed password with static salt: {hashed_password_static}")

dynamic_salt = generate_dynamic_salt()
hashed_password_dynamic = hash_password(password, dynamic_salt)
print(f"Hashed password with dynamic salt: {hashed_password_dynamic}")