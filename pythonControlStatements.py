# Python Control Statements - Activity 1
# Write a Python program that accepts three numbers from the user and prints "Increasing order" if the numbers are in the increasing order, "Decreasing order" if the
# numbers are in the decreasing order, and "Neither increasing or decreasing order" otherwise.
# Declare three integer variables from user input
first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
third_number = int(input("Input third number: "))

# Test if all three variables are equal, print "All numbers are equal" if true
if first_number == second_number == third_number:
    print("All numbers are equal")
# If all numbers are not equal, test if all three variables are different, print "All numbers are different" if true
elif first_number != second_number and first_number != third_number and second_number != third_number:
    print("All numbers are different")
# If all numbers are not equal or different, then print "Neither all are equal nor different"
else:
    print("Neither all are equal nor different")

# Python Control Statements - Activity 2
# Write a Python program that accepts three numbers from the user and prints "Increasing order" if the numbers are in the increasing order, "Decreasing order" if the
# numbers are in the decreasing order, and "Neither increasing or decreasing order" otherwise.
# Declare three integer variables from user input
first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
third_number = int(input("Input third number: "))

# Test if the first number is less than the second number, then less than the third number, if true print "Increasing order"
if first_number < second_number < third_number:
    print("Increasing order")
# Test if the first number is greater than the second number, then greater than the third number, if true print "Decreasing order"
elif first_number > second_number > third_number:
    print("Decreasing order")
# If it is not increasing or decreasing, print "Neither increasing or decreasing"
else:
    print("Neither increasing or decreasing")
