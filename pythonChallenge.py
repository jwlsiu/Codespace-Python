# Python Challenge
# Create a Rock, Paper, and Scissors game in Python without using any external game libraries.
# Import the Random Module to allow us to return a random integer
import random


# Define a function for the Rock, Scissors, Paper game
def rsp_game():
    # Ask user to input a choice of Rock, Paper or Scissors. If invalid choice entered, will ask again until valid.
    while True:
        user_choice = input("Enter a choice (Rock, Paper, Scissors?): ").capitalize()

        if user_choice == "Rock" or user_choice == "Paper" or user_choice == "Scissors":
            break
        else:
            print("Invalid choice, pick again.\n")

    # Return a random number between 1 and 3 and assign each one to either rock, paper or scissor. Declare this as the 'computer choice' variable
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    elif computer_choice == 3:
        computer_choice = "Scissors"

    # Print user's choice and computer's choice
    print(f"You chose {user_choice}, the computer chose {computer_choice}.")

    # Define user and computer scores as global variables so that they can be used outside a function
    global user_score
    global computer_score

    # Use the if...elif...else statements to test for winning and losing combinations. If user wins, add a point to user score. If computer wins, add a point to the
    # computer score. Tie when choices are equal, no points added to either.
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


# Declare user and computer's score as 0 as the start of the game
user_score = 0
computer_score = 0

# Define a function to play the game. It will ask the user if they want to play again. Continue playing if the answer is 'Yes', stop playing and display final scores
# if the answer is 'No'. Ask again if an invalid answer is given.
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

# Run the game
play_game()
