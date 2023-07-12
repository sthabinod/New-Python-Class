# def add_number(xyz,b_parameter): #creating function expecting 2 parameter
#     sum = xyz+b_parameter
#     return sum
    # default return type None


# a_value = int(input("enter first number"))
# b_value = int(input("enter second number"))

# print(add_number(a_value,b_value))

#calling function and sending argument
# add_number(12300,29239)
# add_number(1200,2939)
# add_number(1200,2299)


operation = input("Enter operation...!  \t")
first_number = int(input("Enter first number...! \t"))
second_number = int(input("Enter second number...! \t"))

def add(num_one,num_two):
    sum = num_one+num_two
    return sum

def sub(num_one,num_two):
    subtract = num_one-num_two
    return subtract

#variable scope
if operation=='+':
    name = "Something"
    print(add(first_number,second_number))
    
elif operation=='-':
    print(sub(first_number,second_number))
    
print(name)

