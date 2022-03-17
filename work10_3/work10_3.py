filename = 'guest.txt'

str = input("Please enter you name: ")
with open(filename, 'w') as file_object:
    file_object.write(str)
