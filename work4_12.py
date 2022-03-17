my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for value in range(0, 4):
	print(my_foods[value], end = ' ')

print("\nMy friend's favorite foods are:")
for value in range(0, 4):
	print(friend_foods[value], end = ' ')




