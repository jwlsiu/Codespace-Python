# Python Collections - Activity 1
# Write a Python program to sum values of a list.
# Create an empty list
new_list = []
# Ask user to choose the length of the new list
list_number = int(input("Input length of list: "))
# Ask user to input numbers to create a list. Numbers are added to the list, stopping when reaching the length defined above.
for x in range(list_number):
    new_number=int(input(f"Input number to add create a list ({x + 1}/{list_number}): "))
    new_list.append(new_number)

# Print the new list
print(new_list)
# Sum the numbers in the new list and print result
list_sum = sum(new_list)
print(f"The sum is {list_sum}")

# Python Collections - Activity 2
# Write a Python program to calculate the average value of a list elements.
# Create an empty list
new_list = []
# Ask user to choose the length of the new list
list_number = int(input("Input length of list: "))
# Ask user to input numbers to create a list. Numbers are added to the list, stopping when reaching the length defined above.
for x in range(list_number):
    new_number=int(input(f"Input number to add create a list ({x + 1}/{list_number}): "))
    new_list.append(new_number)

# Print the new list
print(new_list)
# Find the average of the list by summing the list and dividing by the length of list. Round number to 1 decimal place.
average_list = round(sum(new_list) / list_number,1)
# Print the result
print(f"Average value of the list elements is: {average_list}")

# Python Collections - Activity 3
# Write a Python program to find the maximum and minimum value of a list.
# Create an empty list
new_list = []
# Ask user to choose the length of the new list
list_number = int(input("Input length of list: "))
# Ask user to input numbers to create a list. Numbers are added to the list, stopping when reaching the length defined above.
for x in range(list_number):
    new_number=int(input(f"Input number to add create a list ({x + 1}/{list_number}): "))
    new_list.append(new_number)

# Print the list created
print(f"Original list {new_list}")
# Sort the list from smallest to largest
sorted_list = sorted(new_list)
# Minimum value is the first item in the list, maximum is the last item in the list.
min_value = sorted_list[0]
max_value = sorted_list[list_number - 1]
# Print the maximum and minimum value in the list
print(f"Maximum value for the above list = {max_value}")
print(f"Minimum value for the above list = {min_value}")

