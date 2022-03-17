prompt = "Tell us what you want to add in pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

stuff = ""
while stuff != 'quit':
    stuff = input(prompt)
    if stuff != 'quit':
        print("We'll add " + stuff + " in pizza.")
