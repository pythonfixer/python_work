users = ['eric', 'admin', 'mike', 'jack', 'marry']
for user in users:
    if user == 'admin':
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")

length = len(users)
for var in range(0,length):
    del users[len(users)-1]
if len(users) == 0:
    print("We need to find some users!")
    
    
