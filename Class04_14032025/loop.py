# While Loop
msg= "Kharak Singh k Kharaknay say Kharaki hain Khirkiya"
count = 1
while count <= 5:
    print(count, msg)
    count += 1

msg2 = "Want some! Come get some!"
# For Loop
for i in range(6,11):
    print(i, msg2)
    print("-"*30)
    i += 1

# Function which takes unlimited numbers in arguments and returns the sum of all the numbers
# *n is used to take unlimited numbers in arguments, n store all the arguments in a tuple
# if we use **n then it will store all the arguments in a dictionary
def sum_of_numbers(*n):
    sum = 0 # Initialize sum to 0
    for i in n: # Loop through all the arguments
        sum += i # Add each argument to sum
    print(sum) # Print the sum

sum_of_numbers(1,2,3,4,5,6,7,8,9,10)


# Factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Fibonacci series - Recursive implementation
def fibonacci(n):
    # Base case 1: if n is 0, return 0
    # This is the first number in Fibonacci sequence
    if n == 0:
        return 0
    # Base case 2: if n is 1, return 1
    # This is the second number in Fibonacci sequence
    elif n == 1:
        return 1
    # Recursive case: for any other number
    # Calculate sum of previous two numbers in sequence
    # For example: fib(6) = fib(5) + fib(4)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function with n = 6
# This will generate the 6th Fibonacci number
# Sequence will be: 0,1,1,2,3,5,8
print(fibonacci(6))  # Output: 8