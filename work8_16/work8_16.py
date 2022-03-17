import add_numbers
	
num1 = input("Please enter number1: ")
num2 = input("Please enter number2: ")
print(str(num1) + " + " + str(num2) + " = " + add_numbers.add(int(num1), int(num2)))

print("\n")

from add_numbers import add
	
num1 = input("Please enter number1: ")
num2 = input("Please enter number2: ")
print(str(num1) + " + " + str(num2) + " = " + add(int(num1), int(num2)))

print("\n")


from add_numbers import add as a
	
num1 = input("Please enter number1: ")
num2 = input("Please enter number2: ")
print(str(num1) + " + " + str(num2) + " = " + a(int(num1), int(num2)))

print("\n")

import add_numbers as an
	
num1 = input("Please enter number1: ")
num2 = input("Please enter number2: ")
print(str(num1) + " + " + str(num2) + " = " + an.add(int(num1), int(num2)))

print("\n")

from add_numbers import *
	
num1 = input("Please enter number1: ")
num2 = input("Please enter number2: ")
print(str(num1) + " + " + str(num2) + " = " + add(int(num1), int(num2)))

