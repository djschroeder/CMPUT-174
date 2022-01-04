# A class definition characterizes the properties and the
# behavior of a group of objects that are of a certain kind.
import random

class Die:
    def __init__(self,number_of_sides):
        self.sides = number_of_sides  # sides is the instance attribute that represents the property of a Die object
    def roll(self):
        return random.randint(1,self.sides)

# program that uses the Die class
def main ():
    # create an object - an instance of a class
    d6 = Die(6)
    print(d6.roll())
    d8 = Die(8) # 1. object comes into existence 2. init method in the class is called
    print(d8.roll())
    d12 = Die(12)
    print(d12.roll())
main()