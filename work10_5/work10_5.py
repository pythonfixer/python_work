filename = 'reason.txt'

str = input("Why you like programming?\n")
while str != 'q':
    with open(filename, 'a') as file_object:
        file_object.write(str + "\n")
    str = input("Why you like programming?\n")
