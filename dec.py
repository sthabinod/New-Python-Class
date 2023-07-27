# def repeat(num_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(num_times=3)
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Alice")


# split
# text = ["Hello, this is a sample string."]
# words = text.split()
# print(words)

# def add(x,y):
#     return x+y

# add = lambda x, y: x + y
# result = add(3, 5)
# print(result)  # Output: 8

# # kwargs and args


# class Animal:
    
#     def sound(self):
#         print("something..")
    
#     # over loading
#     def task(self,*args):
#         print(args)
        
        
# class Cow(Animal):
    
#     def sound(self):
#         print("Cow make some baw... sound.")

# cow_object = Cow()
# cow_object.sound()
# cow_object.task("hello","Hi","lskdf","lsdjf","sdljf")