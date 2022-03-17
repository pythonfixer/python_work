def show_magicians(names):
    print("\nThe magicians names are:")
    for name in names:
        print(name.title())

def make_great(names):
    great_names = []
    while names:
        name = names.pop()
        name = 'the Great ' + name
        great_names.append(name)

    while great_names:
        name = great_names.pop()
        names.append(name)
        
        
        
magincians_names = ['mike', 'mary', 'bob']
make_great(magincians_names)
show_magicians(magincians_names)
