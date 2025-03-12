# HangMan2
import random

# Dictionary of word categories
word_categories = {
    "Animals": ["elephant", "giraffe", "kangaroo", "dolphin", "penguin"],
    "Fruits": ["banana", "strawberry", "pineapple", "watermelon", "blueberry"],
    "Countries": ["canada", "germany", "brazil", "norway", "thailand"],
}

def choose_category():
    """Allows the user to select a word category."""
    print("\n🌍 Choose a category:")
    categories = list(word_categories.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]  # Return selected category
            else:
                print("⚠️ Invalid choice. Please select a number from the list.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def get_word(category):
    """Randomly selects a word from the chosen category."""
    return random.choice(word_categories[category])

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main function to run the Hangman game."""
    category = choose_category()
    word = get_word(category)  # Select a word from the chosen category
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 6

    print(f"\n🎩 You chose the category: {category}. Try to guess the word!")

    while len(incorrect_guesses) < max_attempts:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"❌ Incorrect guesses ({len(incorrect_guesses)}/{max_attempts}): {' '.join(incorrect_guesses) if incorrect_guesses else 'None'}")
        print("📖 Available letters:", " ".join(sorted(set("abcdefghijklmnopqrstuvwxyz") - guessed_letters - incorrect_guesses)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input! Enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("⚠️ You already guessed that letter! Try again.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("✅ Great! That letter is in the word.")
        else:
            incorrect_guesses.add(guess)
            print("❌ Wrong guess!")

        # Check if the player has guessed all letters
        if set(word) == guessed_letters:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n😞 Game over! The word was:", word)

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing! 👋")

# Run the game
hangman()
