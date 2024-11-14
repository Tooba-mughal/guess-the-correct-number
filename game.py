import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    tries = 10  # number of attempts allowed

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have 10 tries to guess it correctly!")

    for attempt in range(1, tries + 1):
        guess = int(input(f"Attempt {attempt}/{tries}: Enter your guess: "))


        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")

# Run the game
guessing_game()
