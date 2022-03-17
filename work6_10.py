numbers = {
    'Jim': [6, 3, 9],
    'Marry': [7, 5, 2, 1],
    'Mike': [3, 4, 8],
    'Bob': [5, 0, 3, 2, 7],
    'Jack': [9, 1, 0],
    }

for name, nums in numbers.items():
    print(name)
    for num in nums:
        print("\t" + str(num))