prompt = "Tell us how old are you and we'll tell you the value of the ticket:"
prompt += "\n(Enter 'quit' when you are finished.) "

age = ""
while age!= 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if (age >= 0) and (age < 3):
            print("You're free for the ticket.")
        elif (age >= 3) and (age <= 12):
            print("You'll pay $10 for the ticket.")
        elif age > 12:
            print("You'll pay $15 for the ticket.")
        else:
            print("Enter error.")
