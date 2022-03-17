print("Give me two numbers, and I'll add them.")

first_number = input("First number: ")
second_number = input("Second number: ")
try:
    result = int(first_number) + int(second_number)
except ValueError:
    print("Please enter two numbers.")
else:
    print(first_number + " + " + second_number + " = " + str(result))
