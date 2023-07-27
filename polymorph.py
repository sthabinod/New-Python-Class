
class Animal:
    hello = "welcome"
    
    def sound(self,*args):
        for sound in args:
            print(sound)
        
    def welcome(self,hello):
        print(hello)

# method over riding
# with inheritance

class Cow(Animal):
    def welcome(self,hello):
        print("Welcome to the program...")
    
    
    
object = Animal()
object.sound("chirip")
object.sound("Roar","Meow")

cow_object = Cow()
cow_object.welcome("Hello")