current_users = ['eric', 'admin', 'mike', 'jack', 'marry']
new_users = ['bob', 'Mike', 'john', 'lily', 'admin']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("'" + new_user.title() + "' has been used. Need another user name!")
    else:
        print("'" + new_user.title() + "' is not been used.")
