
# Python code to demonstrate how parent constructors
# are called.
 
# parent class
class Person:
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
 
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using its instance
a.display()



# # Must be animal class

# Scenario: Zoo Animals

# You are tasked with designing a Python program to represent various animals in a zoo. The program should follow the Object-Oriented Programming (OOP) concepts of inheritance and polymorphism.

# Create an Animal class with the following attributes and methods:

# Attributes: name, species, habitat
# Methods: make_sound() - Prints a generic sound that all animals make.
# Implement the following child classes inheriting from the Animal class:
# a. Mammal: Inherits from Animal.
# b. Amphibian: Inherits from Animal.
# c. Reptile: Inherits from Animal.

# Override the make_sound() method in each child class to provide a unique sound that each type of animal makes.

# Create a polymorphic function called animal_in_zoo_sound(animal_obj) that takes an Animal object as an argument and calls the make_sound() method on that object.

# Question:

# Design the Python classes Animal, Mammal, Amphibian, and Reptile based on the above scenario. Implement the inheritance and polymorphism concept by overriding the make_sound() method in each child class. Finally, write a polymorphic function animal_in_zoo_sound(animal_obj) that can accept any Animal object and call its make_sound() method.

# Demonstrate the implementation by creating instances of each class, calling the make_sound() method, and using the animal_in_zoo_sound() function.



# Parent class: Animal
# class Animal:
#     def __init__(self, name, species, habitat):
#         self.name = name
#         self.species = species
#         self.habitat = habitat

#     def make_sound(self):
#         print("Generic animal sound.")

# # Child class: Mammal
# class Mammal(Animal):
#     def make_sound(self):
#         print("Roar! I'm the king of the jungle!")

# # Child class: Amphibian
# class Amphibian(Animal):
#     def make_sound(self):
#         print("Croak Croak!")

# # Child class: Reptile
# class Reptile(Animal):
#     def make_sound(self):
#         print("Sssss!")

# # Polymorphic function
# def animal_in_zoo_sound(animal_obj):
#     animal_obj.make_sound()

# # Create instances of each class
# lion = Mammal("Lion", "Panthera leo", "Savannah")
# frog = Amphibian("Frog", "Rana temporaria", "Pond")
# snake = Reptile("Snake", "Python regius", "Desert")

# # Demonstrate the unique sounds of each animal
# lion.make_sound()  # Output: Roar! I'm the king of the jungle!
# frog.make_sound()  # Output: Croak Croak!
# snake.make_sound()  # Output: Sssss!

# # Using the polymorphic function to call make_sound()
# animal_in_zoo_sound(lion)  # Output: Roar! I'm the king of the jungle!
# animal_in_zoo_sound(frog)  # Output: Croak Croak!
# animal_in_zoo_sound(snake)  # Output: Sssss!