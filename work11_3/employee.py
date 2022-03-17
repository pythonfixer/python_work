class Employee():
    
    def __init__(self, first, last, money):
        self.first = first.title()
        self.last = last.title()
        self.money = money
        
    def give_raise(self, raise_money=5000):
        self.money += raise_money 
