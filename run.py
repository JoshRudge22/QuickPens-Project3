import random
import time

def print_one_letter_at_a_time(text):
    """Prints text one letter at a time with a slight delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)

ascii_art = """
████████▄   ███    █▄   ▄█   ▄████████    ▄█   ▄█▄
███    ███  ███    ███ ███  ███    ███   ███ ▄███▀
███    ███  ███    ███ ███▌ ███    █▀    ███▐██▀
███    ███  ███    ███ ███▌ ███         ▄█████▀
███    ███  ███    ███ ███▌ ███        ▀▀█████▄
███    ███  ███    ███ ███  ███    █▄    ███▐██▄
███  ▀ ███  ███    ███ ███  ███    ███   ███ ▀███▄
 ▀██████▀▄█ ████████▀  █▀   ████████▀    ███   ▀█▀
   ▄███████▄    ▄████████ ███▄▄▄▄      ▄████████
  ███    ███   ███    ███ ███▀▀▀██▄   ███    ███
  ███    ███   ███    █▀  ███   ███   ███    █▀
  ███    ███  ▄███▄▄▄     ███   ███   ███
▀█████████▀  ▀▀███▀▀▀     ███   ███ ▀███████████
  ███          ███    █▄  ███   ███          ███
  ███          ███    ███ ███   ███    ▄█    ███
 ▄████▀        ██████████  ▀█   █▀   ▄████████▀
"""

def get_input(prompt, valid_choices):
    """Get user input and ensure it is valid."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print(f"Invalid choice. Please choose a number from {valid_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_yes_no_input(prompt):
    """Get user input and ensure it is 'yes' or 'no'."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['yes', 'no']:
            return choice
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def get_heads_or_tails_input(prompt):
    """Get user input and ensure it is 'heads' or 'tails'."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['heads', 'tails']:
            return choice
        else:
            print("Invalid choice. Please enter 'heads' or 'tails'.")

def coin_toss():
    """Simulate a coin toss."""
    return random.choice(["heads", "tails"])

def player_shoots(name):
    """Simulate the player taking a penalty shot."""
    player_choice = get_input("Choose either '1', '2', '3', '4', '5': \n", [1, 2, 3, 4, 5])
    computer_choice = random.choice([1, 2, 3, 4, 5])

    print(f"{name} has gone for {player_choice} \n")
    time.sleep(0.5)
    print(f"Computer dives to {computer_choice} \n")
    time.sleep(0.5)

    if player_choice == computer_choice:
        print("Keeper with the SAVVVVEEEE!!!!!!!! \n")
        return False
    else:
        print(f"{name} with the GGGOOOOOAALLLLL \n")
        return True

def player_saves(name):
    """Simulate the player trying to save a penalty shot."""
    player_choice = get_input("Dive to either '1', '2', '3', '4', '5': \n", [1, 2, 3, 4, 5])
    computer_choice = random.choice([1, 2, 3, 4, 5])

    print(f"Computer has gone for {computer_choice} \n")
    time.sleep(0.5)
    print(f"{name} dives to {player_choice} \n")
    time.sleep(0.5)

    if player_choice == computer_choice:
        print(f"{name} with the SAVVVVEEEE!!!!!!!! \n")
        return True
    else:
        print("Computer with the GGGOOOOOAALLLLL \n")
        return False

def game(name, first_shooter):
    player_goals = 0
    computer_goals = 0

    for i in range(5):
        print(f"Round {i+1}:")
        if first_shooter == "player":
            print(f"{name} takes the shot!")
            if player_shoots(name):
                player_goals += 1
            print(f"Score update: {name} {player_goals} - Computer {computer_goals}")
            print(f"{name} tries to save!")
            if not player_saves(name):
                computer_goals += 1
            print(f"Score update: {name} {player_goals} - Computer {computer_goals}")
        else:
            print(f"{name} tries to save!")
            if not player_saves(name):
                computer_goals += 1
            print(f"Score update: {name} {player_goals} - Computer {computer_goals}")
            print(f"{name} takes the shot!")
            if player_shoots(name):
                player_goals += 1
            print(f"Score update: {name} {player_goals} - Computer {computer_goals}")

    return player_goals, computer_goals

def main():
    print_one_letter_at_a_time(ascii_art)
    if get_yes_no_input("Can you step up? (yes/no): \n") == 'yes':
        name = input("Please enter your name: \n").strip()
        while not name:
            print("Name cannot be empty. Please enter a valid name.")
            name = input("Please enter your name: \n").strip()

        nationality = input(f"Please can {name} enter the country they represent: \n").strip()
        while not nationality:
            print("Country cannot be empty. Please enter a valid country.")
            nationality = input(f"Please can {name} enter the country they represent: \n").strip()

        intro_text = f"""
We have {name} from {nationality}
            
It's 0-0 after a dull 120 minutes of Football, your country is
relying on you to bring home the world cup. 
            
Aim is to pick a number different to the computer in order to score.
If you and the computer both have the same number, the computer makes the save.
If you and the computer both pick different numbers, then you score.
Example: if you type 2 and the computer types 3, you've scored a goal. 
However, if you type 1 and the computer types 1, then the computer makes the save.
You can go 1 = top left, 2 = bottom left, 3 = middle, 4 = top right, and 5 = bottom right.
Please don't let your country down. Don't be a Harry Kane!
Let's start with {nationality} vs Germany in a penalty shootout!!!
"""
        print_one_letter_at_a_time(intro_text)

        player_choice = get_heads_or_tails_input("Heads or Tails? \n")
        toss_result = coin_toss()
        print(f"The coin toss result is {toss_result}.\n")

        if player_choice == toss_result:
            print("You won the coin toss! Do you want to take the first penalty? (yes/no): \n")
            if get_yes_no_input("") == "yes":
                first_shooter = "player"
            else:
                first_shooter = "computer"
        else:
            first_shooter = "computer"
            print("Computer won the coin toss and will take the first penalty.\n")

        while True:
            player_goals, computer_goals = game(name, first_shooter)
            print("That's all they needed! \n")
            
            if player_goals > computer_goals:
                print(f"{name} has won it for {nationality}! What a legend!")
            else:
                print(f"Computer breaks the hearts of {nationality}")

            play_again = get_yes_no_input("Fancy another go? (yes/no): \n")
            if play_again != 'yes':
                break
        
        print("All the best buddy!")

    else:
        print("Okay then, enjoy your day.")

if __name__ == "__main__":
    main()