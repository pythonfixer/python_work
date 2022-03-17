import json

def get_stored_number():
    filename = 'number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
            return None
    else:
            return number
            
def get_new_number():
    number = input("What is your favorite number? ")
    filename = 'number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number
    
def read_number():
    number = get_stored_number()
    if number:
        print("I know your favorite number! It's " + number + ".")
    else:
        number = get_new_number()
        print("OK! You've entered your favorite number.")
        
read_number()
    
