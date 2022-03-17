squares3 = [value ** 3 for value in range(1, 11)]
print(squares3)
print("The first three items in the list are:")
for square in squares3[:3]:
	print(square)
print("Three items from the middle of the list are:")
for square in squares3[3:6]:
	print(square)
print("The last three items in the list are:")
for square in squares3[-3:]:
	print(square)
