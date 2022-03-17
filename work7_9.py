sandwich_orders =  ['pastrami', 'tuna', 'pastrami', 'tomato', 'pastrami']
finished_sandwiches = []

print("The pastrami has been sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)
    
print("\nThe following sandwiches have been finished:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title() + " Sandwich")
