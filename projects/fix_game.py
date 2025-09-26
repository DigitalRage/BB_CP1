# BB 1st Fix the Game Project
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) # The number wasn't converted to an integer, so I did it
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess: # This was an if, now it's an elif
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1 # Added attempts += 1 to make the attempt variable go up. 
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1 # Added attempts += 1 to make the attempt variable go up. 
        continue
    print("Game Over. Thanks for playing!")
start_game()