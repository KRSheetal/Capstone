import random #import random

class Dice:
    def __init__(self, sides=6): #for predefined sides
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides) #picks random number in the range
    
'''dice = Dice(4)
for roll in range(10):
    print(dice.roll())'''

dice2 = Dice()
#for roll in range(6):
print(dice2.roll()) #prints a random number