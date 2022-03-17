names = ['mike', 'bob', 'tom']
print(names[0].title() + ', ' + names[1].title() + ' and ' + names[2].title() + ', please stay for supper.') 
print(names[2].title() + ' cannot stay for supper.')
names[2] = 'jack'
print(names[0].title() + ', ' + names[1].title() + ' and ' + names[2].title() + ', please stay for supper.') 

print("I have found a bigger table.")
names.insert(0, "emma")
names.insert(2, "may")
names.append("kate")
print(names[0].title() + ', ' + names[1].title() + ', ' + names[2].title() + ', '+ names[3].title() + ', ' + names[4].title() + ' and ' + names[5].title() + ', please stay for supper.')

print("Only two person could be stay for supper.")
name_pop = names.pop()
print(name_pop.title() + ", sorry you cannot stay for supper.")
name_pop = names.pop()
print(name_pop.title() + ", sorry you cannot stay for supper.")
name_pop = names.pop()
print(name_pop.title() + ", sorry you cannot stay for supper.")
name_pop = names.pop()
print(name_pop.title() + ", sorry you cannot stay for supper.")
print(names[0].title() + ', you will still stay for supper.')
print(names[1].title() + ', you will still stay for supper.')
del names[1]
del names[0]
print(names)


