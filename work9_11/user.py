class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        
    def describe_user(self):
        print("\n" + self.first_name.title() + " " + self.last_name.title())
        print(self.user_info)
        
    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()
