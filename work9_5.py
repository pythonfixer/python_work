class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0
        
        
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title())
        print(self.user_info)
        
    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
mike = User('mike', 'green', country = 'usa')
mike.describe_user()
mike.greet_user() 
jim = User('jim', 'brown', location = 'new york', country = 'usa')
jim.describe_user()
jim.greet_user() 
mary = User('mary', 'white', age = '22', tel = '86513370', email = 'mary@gmail.com')
mary.describe_user()
mary.greet_user()

print("\n")

steve = User('steve', 'jobs', fax = '81235126')
for i in range(1,6):
    steve.increment_login_attempts()
    print(steve.login_attempts)
steve.reset_login_attempts()
print(steve.login_attempts)

