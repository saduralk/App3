import json

userList = [
    {
        "name": "Alice",
        "age": 25,
        "role": "admin"
    },
    {
        "name": "Bob",
        "age": 30,
        "role": "user"
    }
]

def get_users_over_30(users):
    return [user for user in users if user["age"] >= 30]

with open("users.json", "w") as file:
    json.dump(userList, file)

with open("users.json", "r") as file:
    loaded_users = json.load(file)
    print(f"Loaded_users: {loaded_users}")
    print(f"Type of loaded_users: {type(loaded_users)}")
    print(f"Users over 30: {get_users_over_30(loaded_users)}")
# ---------------------------------------------------------------------------------------- #
#converted = json.dumps(user) # Note to self: this is a JSON string, not a Python object
#print("Converted object: " + converted)
#print("Type of converted object: " + str(type(converted)))
#backToPython = json.loads(converted) # Note to self: converted back into Python dictionary
#print(f"Type of backToPython object: {type(backToPython)}")
#print("Name: " + backToPython["name"])
# ---------------------------------------------------------------------------------------- #