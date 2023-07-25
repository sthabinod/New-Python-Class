
class Animal:
    hello = "welcome"
    def sound(self,my_sound):
        print("My sound....", my_sound)
    
    # over load
    def sound(self,hello):
        print(hello)   
    
    
    def welcome(self,hello):
        print(hello)

# method over riding
# with inheritance

class Cow(Animal):
    def welcome(self,hello):
        print("Welcome to the program...")
    
    
    
object = Animal()
object.sound("chirp")

cow_object = Cow()
cow_object.welcome("Hello")