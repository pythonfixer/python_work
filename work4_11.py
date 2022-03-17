pizzas = ['pizza1', 'pizza2', 'pizza3']
friend_pizzas = pizzas[:]

pizzas.append('pizza_new')
friend_pizzas.append('pizza_another')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
	
print("I really love pizza!")

