from art import logo
import random

num_attempts_easy = 10
num_attempts_difficult = 5


def comments(actual_num, guess_number,attempts):
    if attempts == 1:
        if(actual_num != guess_number):
            print("You have guessed the wrong number again!")
            print("All your guesses are over! Better luck next time:)")
        return True
    elif guess_number < actual_num:
        print("Too Low")
        print("Guess Again")
        return False
    elif guess_number > actual_num:
        print("Too High")
        print("Guess Again")
        return False
    else:
        print(f"You got it! The answer was {guess_number}")
        return True


def game(actual_num, difficulty_level):
    if difficulty_level == 'easy':
        attempts = num_attempts_easy
    else:
        attempts = num_attempts_difficult
    isgameover = False
    while attempts != 0 and not isgameover:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if(comments(actual_num, guess,attempts) == True):
            isgameover = True
        attempts = attempts - 1

print(logo)

print("Welcome to the number guessing game....")
print("I'm thinking of a number between 1 and 100.")
should_continue = True
while should_continue:
    difficuly_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    thinking_number = random.randint(1, 100)
    game(thinking_number, difficuly_level)
    response = input("Do you want to play again 'y' or 'n' : ")
    if response == 'y':
        should_continue = True
    else:
        should_continue = False

print("Thanks for playing my game!")


