users = {
    'vangogh': {
        'first': 'vincent',
        'last': 'van gogh',
        'location': 'nuenen',
        'profession': 'artist',
        },
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'profession': 'physicist',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'profession': 'chemist',
        },
    }
    
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    profession = user_info['profession']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    print("\t\tProfession: " + profession.title())
    
