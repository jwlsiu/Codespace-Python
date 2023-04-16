# Python Functions - Activity 1
# Write 2 Python functions to show the list content and find the max value in the list
# Create and empty list
my_list = []

# Define a function that asks users to create a 5 numbered list and print
def new_list():
    for x in range(5):
        num = int(input("Input number to add to list: "))
        my_list.append(num)
    return print(f"The content of the list is: {my_list}")

# Define a function that finds the maximum value from a list, using the Max function
def list_max_value():
    max_value = max(my_list)
    return print(f"The max value in the list: {max_value}")

# Call the two functions
new_list()
list_max_value()

# Python Functions - Activity 2
# Write a Python function to calculate the factorial of a number (a non-negative integer n ). The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
    elif n == 0:
        print("The factorial of 0 is: 1")
    else:
        answer = 1
        for i in range(1, n+1):
            answer *= i
        print(f"The factorial of {n} is: {answer}")

# Call the function, argument can be changed to chosen number to find the factorial of it
factorial(6)

# Python Functions - Activity 3
# Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime():
    num = int(input("Enter a whole number to check if prime: "))
    # If loop to check if the number entered is 0 or 1
    if num == 0 or num == 1:
        print("Prime numbers need to be a whole number greater than 1")
    # If number is 2
    elif num == 2:
        print(f"{num} is a prime number.")
    # If number is greater than two, check if the modulus is equal to zero for numbers between 2 and num - 1. Not prime if true, prime if false.
    elif num > 2:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} is not a prime number.")
                break
            else:
                print(f"{num} is a prime number.")
                break
            i += 1
    # All other numbers are negative
    else:
        print("Negative numbers are not prime numbers.")


prime()
