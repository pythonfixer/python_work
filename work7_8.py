sandwich_orders =  ['tuna', 'pastrami', 'tomato']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)
    
print("\nThe following sandwiches have been finished:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title() + " Sandwich")
