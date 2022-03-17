def make_sandwich(*stuffs):
	print("\nThis sandwich include:")
	for stuff in stuffs:
		print("- " + stuff)
	
make_sandwich('mushrooms', 'olives')
make_sandwich('green peppers', 'pepperoni', 'french fries')
make_sandwich('extra cheese', 'pineapple')
