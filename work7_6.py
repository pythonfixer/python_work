prompt = "Tell us what you want to add in pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

stuff = ""
while stuff != 'quit':
    stuff = input(prompt)
    if stuff != 'quit':
        print("We'll add " + stuff + " in pizza.")
        
print("\n")

active = True
while active:
    stuff = input(prompt)
    if stuff == 'quit':
        active = False
    else:
        print("We'll add " + stuff + " in pizza.")

print("\n")

while True:
    stuff = input(prompt)
    if stuff == 'quit':
        break
    else:
        print("We'll add " + stuff + " in pizza.")
