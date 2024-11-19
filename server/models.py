import json

class User:
    def __init__(self, email, age):
        self.email = email
        self.age = age

    def to_dict(self):
        return {'email': self.email, 'age': self.age}

def save_users(users):
    with open('users.txt', 'w') as f:
        json.dump(users, f)

def load_users():
    try:
        with open('users.txt', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
