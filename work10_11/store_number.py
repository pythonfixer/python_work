import json

username = input("What is your favorite number? ")

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("OK! You've entered your favorite number.")
