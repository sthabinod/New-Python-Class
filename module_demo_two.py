from demo_package import module_demo_one
from demo_package.module_demo_three import sub

from random import randint
from datetime import datetime


print(module_demo_one.sum(10,20))
print(sub(10,334))
object_animal = module_demo_one.Animal()

print(datetime.now())