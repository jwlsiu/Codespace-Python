# Python Basics - Activity 1
print(-5+8*6)
print((55+9)%9)
print(20+-3*5/8)
print(5+15/3*2-8%3)

# Python Basics - Activity 2
first_number = int(input("Input the first number: "))
second_number = int(input("Input the second number: "))
divide = int(first_number / second_number)
print(f"The division of the first number and the second number is: {divide}")

#Python Control Statements - Activity 1
first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
third_number = int(input("Input third number: "))

if first_number == second_number == third_number:
    print("All numbers are equal")
elif first_number != second_number and first_number != third_number and second_number != third_number:
    print("All numbers are different")
else:
    print("Neither all are equal nor different")

# Python Control Statements - Activity 2
first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
third_number = int(input("Input third number: "))

if first_number < second_number < third_number:
    print("Increasing order")
elif first_number > second_number > third_number:
    print("Decreasing order")
else:
    print("Neither increasing or decreasing")

# Python Loops - Activity 13
x,y = 0,1
while y < 50:
    print(y)
    x,y = y, x+y

chosen_number = int(input("Input a number: "))
for i in range(1,11):
    answer = i*chosen_number
    print(f"{chosen_number} x {i} = {answer}")

Python Collections - Activity 1
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(x))

new_list = []
for x in range(10):
    new_number=int(input("Input number to add create a list: "))
    new_list.append(new_number)

print(new_list)
list_sum = sum(new_list)
print(f"The sum is {list_sum}")

# Python Collections - Activity 2
new_list = []
for x in range(7):
    new_number = int(input("Input number to add create a list: "))
    new_list.append(new_number)

print(new_list)
average_list = round(sum(new_list)/len(new_list),1)
print(f"Average value of the list elements is: {average_list}")

# Python Collections - Activity 3
new_list = []
for x in range(10):
    new_number = int(input("Input number to add create a list: "))
    new_list.append(new_number)

print(f"Original list {new_list}")
sorted_list = sorted(new_list)
print(sorted_list)
min_value = sorted_list[0]
max_value = sorted_list[9]
print(f"Maximum value for the above list = {max_value}")
print(f"Minimum value for the above list = {min_value}")

# Python Functions - Activity 1
my_list = []


def new_list():
    for x in range(5):
        num = int(input("Input number to add to list: "))
        my_list.append(num)
    return print(f"The content of the list is: {my_list}")


def list_max_value():
    max_value = max(my_list)
    return print(f"The max value in the list: {max_value}")


new_list()
list_max_value()

# Python Functions - Activity 2
def factorial():
    n = int(input("Pick a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers")
    elif n == 0:
        print("The factorial of 0 is: 1")
    else:
        answer = 1
        for i in range(1, n+1):
            answer *= i
        print(f"The factorial of {n} is: {answer}")

factorial()

# Python Functions - Activity 3

# Python Challenge

import random


def rsp_game():
    while True:
        user_choice = input("Enter a choice (Rock, Paper, Scissors?): ").capitalize()

        if user_choice == "Rock" or user_choice == "Paper" or user_choice == "Scissors":
            break
        else:
            print("Invalid choice, pick again.\n")

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    elif computer_choice == 3:
        computer_choice = "Scissors"

    print(f"You chose {user_choice}, the computer chose {computer_choice}.")

    global user_score
    global computer_score

    if user_choice == "Rock" and computer_choice == "Scissors":
        print(f"{user_choice} smashes {computer_choice}! You win. \n")
        user_score += 1

    elif user_choice == "Rock" and computer_choice == "Paper":
        print(f"{computer_choice} covers {user_choice}! You lose. \n")
        computer_score += 1

    elif user_choice == "Paper" and computer_choice == "Scissors":
        print(f"{computer_choice} cut {user_choice}! You lose. \n")
        computer_score += 1

    elif user_choice == "Paper" and computer_choice == "Rock":
        print(f"{user_choice} covers {computer_choice}! You win. \n")
        user_score += 1

    elif user_choice == "Scissors" and computer_choice == "Rock":
        print(f"{computer_choice} smashes {user_choice}! You lose. \n")
        computer_score += 1

    elif user_choice == "Scissors" and computer_choice == "Paper":
        print(f"{user_choice} cut {computer_choice}! You win. \n")
        user_score += 1

    else:
        print(f"Both players selected {user_choice}. It's a tie! \n")


user_score = 0
computer_score = 0


def play_game():
    rsp_game()

    while True:
        play_again = input("Do you want to play again? (Yes, No): ").capitalize()
        if play_again == "Yes":
            rsp_game()
        elif play_again == "No":
            print(f"Final Scores: \n Computer: {computer_score} \n Player: {user_score} ")
            break
        else:
            print("Invalid choice, pick again. \n")


play_game()
