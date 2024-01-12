import os

# ANSI codes for text colors
RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
YELLOW = "\u001b[33m"
RESET = "\x1b[0m"

# Constants for choices
ROCK = 1
PAPER = 2
SCISSORS = 3

# Function to clear terminal screen
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Function to pause and wait for the user to press Enter
def confirm():
    input("\nPress Enter to continue...")

#Function to get a valid choice from the user
def get_valid_choice(player):
    while True:
        try:
            print(player)
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            choice = int(input("\nSelect [1-3]: "))
            if choice not in [ROCK, PAPER, SCISSORS]:
                raise ValueError(RED + "Invalid input" + RESET)
            return choice
        except ValueError:
            clear_screen()
            print(RED + "Invalid input. Please enter a valid choice (1-3)." + RESET)

# Define the game outcomes using a dictionary
outcomes = {
    (ROCK, SCISSORS): "Rock breaks scissors",
    (PAPER, ROCK): "Paper covers rock",
    (SCISSORS, PAPER): "Scissors cut paper",
}

# Function to determine the winner based on player choices
def determine_winner(choice_1, choice_2):
    if choice_1 == choice_2:
        return "TIE! No points awarded."
    elif (choice_1, choice_2) in outcomes:
        return f"Player 1 wins! \n{outcomes[(choice_1, choice_2)]}"
    else:
        return f"Player 2 wins! \n{outcomes[(choice_2, choice_1)]}"

# Main menu function
def main_menu():
    p1_count = 0
    p2_count = 0

    while True:
        print(YELLOW + "\n    SCORE    ")
        print("=" * 15)
        print(f"\nPlayer 1: {p1_count} \n")
        print(f"Player 2: {p2_count} \n")
        print("=" * 15 + RESET)
        confirm()
        clear_screen()

        choice_1 = get_valid_choice(BLUE + "\nPlayer #1 choose.\n" + RESET)
        clear_screen()
        choice_2 = get_valid_choice(GREEN + "\nPlayer #2 choose. \n" + RESET)
        clear_screen()
        result = determine_winner(choice_1, choice_2)

        clear_screen()
        print(result)

        if "Player 1" in result:
            p1_count += 1
        if "Player 2" in result:
            p2_count += 1

        while True:
            play_again = input("\nPlay again? (yes/no) ").strip().lower()
            if play_again in ("yes", "no"):
                break
            else:
                clear_screen()
                print(RED + "invalid input. Please enter 'yes' or 'no'." + RESET)
        if play_again == "no":
            break

if __name__ == "__main__":
    main_menu()
