def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# The value is store in stack
# The values are popped
# The values are added

# Test the factorial function
print(factorial(5))  # Output: 120