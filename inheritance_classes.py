class Mammal:
    
    def __init__(self,legs,eyes,name):
        self.legs = legs
        self.eyes = eyes
        self.name = name
    
    def greeting(self):
        print("Hello, welcome mammals!")

class HumanBeing(Mammal):
    welcome  = 'Hello '
    
    def __init__(self,brain_power,eyes,legs,name):
        self.brain_power = brain_power
        super().__init__(eyes,legs,name)
        
    def print_details(self):
        print(f'Name is: {self.name},Eyes: {self.eyes},Legs: {self.legs}, Brain power {self.brain_power}%')


oshan_object = HumanBeing("100","2","2","Oshan")
oshan_object.print_details()
oshan_object.greeting()


