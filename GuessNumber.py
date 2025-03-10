import random

def guess_the_number():
    print("🌟 Welcome to the Guess the Number Game! 🌟")
    print("I have chosen a secret number between 1 and 100. Can you guess it?")
   
 
 
   # The computer selects a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Count the number of guesses

    while True:
        try:
            # The player enters their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increase attempt count
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again. 📉")
            elif guess > secret_number:
                print("Too high! Try again. 📈")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} tries! 🎉")
                print("Your reward: A story of patience and wisdom. 📖✨")
                break  # Exit the loop when guessed correctly
        except ValueError:
            print("Oops! Please enter a valid number.")

# Run the game
guess_the_number()

