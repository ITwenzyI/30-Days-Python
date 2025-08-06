users = {
    "user1": {
        "name": "user1",
    },
    "user2": {
        "name": "user2",
    }
}

def add_user(name, age):
    users[name] = {
        "name": name,
        "age": age,
    }



add_user("Kilian", 19)
print(users)