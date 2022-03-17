from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        x = randint(1, self.sides)
        print(x)
        
die_6 = Die()
die_6.roll_die()

die_10 = Die()
die_10.sides = 10
die_10.roll_die()
  
die_20 = Die()
die_20.sides = 20
die_20.roll_die()
        
