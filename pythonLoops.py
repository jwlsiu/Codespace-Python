# Python Loops - Activity 1
# Write a Python program to get the Fibonacci series between 0 to 50.
# Declare first two numbers in the Fibonacci sequence as 0 and 1, then print
x, y = 0, 1
print(x)
print(y)

# Loop while the sum of x and y are less than 50, print number
while x + y < 50:
    print(x + y)
    # x becomes y and y becomes x + y
    x, y = y, x + y

# Python Loops - Activity 2
# Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Ask user to input a number to create multiplication table
chosen_number = int(input("Input a number: "))
# Create a For Loop to multiply the input number with each number from 1 to 10, then print result.
for i in range(1,11):
    answer = i * chosen_number
    print(f"{chosen_number} x {i} = {answer}")
