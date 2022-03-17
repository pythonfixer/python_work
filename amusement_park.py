age = 12

if age < 4:
    print("You admission cost is $0.")
elif age < 18:
    print("You admission cost is $5.")
else:
    print("You admission cost is $10.")

print("\n")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("You admission cost is $" + str(price) + ".")

print("\n")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("You admission cost is $" + str(price) + ".")        

print("\n")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("You admission cost is $" + str(price) + ".")        
