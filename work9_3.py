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

jim = User('jim', 'green', country = 'usa')
jim.describe_user()
jim.greet_user()

mike = User('mike', 'brown', location = 'new york', country = 'canada')
mike.describe_user()
mike.greet_user()

mary = User('mary', 'white', age = '20', tel = '80523655', email = 'mary@gmail.com')
mary.describe_user()
mary.greet_user()
