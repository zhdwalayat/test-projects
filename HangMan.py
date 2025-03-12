import random

# List of words for the game
word_list = ["python", "hangman", "developer", "challenge", "programming"]

def get_word():
    """Randomly selects a word from the list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main function to run the Hangman game."""
    word = get_word()  # Select a random word
    guessed_letters = set()  # Store correct guesses
    incorrect_guesses = set()  # Store incorrect guesses
    max_attempts = 6  # Number of wrong attempts allowed

    print("🎩 Welcome to Hangman! Try to guess the word.")
    
    while len(incorrect_guesses) < max_attempts:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"❌ Incorrect guesses ({len(incorrect_guesses)}/{max_attempts}): {' '.join(incorrect_guesses)}")
        
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input! Enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("⚠️ You already guessed that letter! Try again.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("✅ Good guess!")
        else:
            incorrect_guesses.add(guess)
            print("❌ Wrong guess!")

        # Check if all letters are guessed
        if set(word) == guessed_letters:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n😞 Game over! The word was:", word)

# Run the game
hangman()
