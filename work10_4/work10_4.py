filename = 'guest_book.txt'

str = input("Please enter you name: ")
while str != 'q':
    print("Nice to meet you " + str + "!")
    with open(filename, 'a') as file_object:
        file_object.write(str + " had attend this meeting.\n")
    str = input("Please enter your name: ")
