import random

class User:
    name = ""
    age = -1
    email = ""
    def __init__(self, name, age, email, userID):
        self.name = name
        self.age = age
        self.email = email
        self.userID = userID


def generateUsers(count):
    DEFAULT_NAMES = ["Alice", "Bob", "Charlie", "Dex", "Ellen", "Fred"]
    users = []
    for foo in range(count):
        _name = DEFAULT_NAMES[random.randint(0, len(DEFAULT_NAMES))]
        users.append(User(
            _name,
            random.randint(0, 100),
            "{}{}@email.com".format(_name, random.randint(0,1000)),
            foo
        ))
    return users
