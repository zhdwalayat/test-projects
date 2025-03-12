import random

def get_user_choice():
    """Get the user's choice."""
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        return get_user_choice()  # Recursively ask again if input is invalid
    return user_choice

def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    """Decide the winner based on the game rules."""
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def play_game():
    """Run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        print(determine_winner(user_choice, computer_choice))

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thanks for playing! Goodbye! 👋")
            break

# Run the game
play_game()
