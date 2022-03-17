def show_magicians(names):
    print("\nThe magicians names are:")
    for name in names:
        print(name.title())

def make_great(names):
    great_names = []
    names_bak = []
    while names:
        name = names.pop()
        name = 'the Great ' + name
        great_names.append(name)

    while great_names:
        name = great_names.pop()
        names_bak.append(name)
    return names_bak
        
        
        
magincians_names = ['mike', 'mary', 'bob']
bak = []
bak = make_great(magincians_names[:])
show_magicians(magincians_names)
show_magicians(bak)
