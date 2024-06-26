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
                print(
                    f"Invalid choice. "
                    f"Please choose a number from {valid_choices}."
                )
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
    player_choice = get_input(
        "Choose either '1', '2', '3', '4', '5': \n", [1, 2, 3, 4, 5]
    )
    computer_choice = random.choice([1, 2, 3, 4, 5])

    print(f"{name} has gone for {player_choice} \n")
    time.sleep(0.5)
    print(f"Computer dives to {computer_choice} \n")
    time.sleep(0.5)

    if player_choice == computer_choice:
        print("Neuer with the SAVVVVEEEE!!!!!!!! \n")
        return False
    else:
        print(f"{name} with the GGGOOOOOAALLLLL \n")
        return True

def player_saves(name):
    """Simulate the player trying to save a penalty shot."""
    player_choice = get_input(
        "Dive to either '1', '2', '3', '4', '5': \n", [1, 2, 3, 4, 5])
    computer_choice = random.choice([1, 2, 3, 4, 5])

    print(f"Computer goes {computer_choice} \n")
    time.sleep(0.5)
    print(f"{name} dives to {player_choice} \n")
    time.sleep(0.5)

    if player_choice == computer_choice:
        print(f"{name} with the SAVVVVEEEE!!!!!!!! \n")
        return True
    else:
        print("Muller with the GGGOOOOOAALLLLL \n")
        return False

def game(name, nation, first_shooter):
    player_goals = 0
    computer_goals = 0

    for i in range(5):
        print(f"Round {i+1}:")
        if first_shooter == "player":
            print(f"{name} steps up to take it!")
            if player_shoots(name):
                player_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")
            print(f"{name} now needs to make themselves look big!")
            if not player_saves(name):
                computer_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")
        else:
            print(f"{name} tries to save!")
            if not player_saves(name):
                computer_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")
            print(f"{name} takes the shot!")
            if player_shoots(name):
                player_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")

        if player_goals >= 5 or computer_goals >= 5:
            break

    while player_goals == computer_goals:
        print("Sudden Death Round:")
        if first_shooter == "player":
            print(f"{name} steps up to take it {name} goes!")
            if player_shoots(name):
                player_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")
            print(f"{name} now needs to make themselves look big!")
            if not player_saves(name):
                computer_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")
        else:
            print(f"{name} tries to save!")
            if not player_saves(name):
                computer_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")
            print(f"{name} takes the shot!")
            if player_shoots(name):
                player_goals += 1
            print(f"Score update: {nation} "
                  f"{player_goals} - Germany {computer_goals}")

    return player_goals, computer_goals

def main():
    print_one_letter_at_a_time(ascii_art)
    if get_yes_no_input("Can you step up? (yes/no): \n") == 'yes':
        name = input("Please enter your name: \n").strip()
        while not name.isalpha():
            print("Name must be letters only. Please enter a valid name.")
            name = input("Please enter your name: \n").strip()

        nation = input(f"Please can {name} "
                       f"enter the country they represent: \n").strip()
        while not nation.isalpha():
            print("Country must be letters only. "
                  f"Please enter a valid country.")
            nation = input(f"Please can {name} enter "
                           f"the country they represent: \n").strip()

        intro_text = f"""
We have {name} from {nation}

It's 0-0 after a dull 120 minutes of Football, your country is
relying on you to bring home the world cup.

To start off you need to win heads or tails to decide who takes
the first penalties. Once that has been decided you and the computer
will have 5 penalties each to take, whoever scores the most out of
5 penalties wins the game. If the 5 penalties have been taken and its
a draw we go to sudden death to decide!

Rules:
Aim is to pick a number different to the computer in order to score.
If you and the computer both have the same number, the computer makes the save.
If you and the computer both pick different numbers, then you score.
Example: if you type 2 and the computer types 3, you've scored a goal.
However, if you type 1 and the computer types 1,
then the computer makes the save.
You can go 1 = top left, 2 = bottom left,
3 = middle, 4 = top right, and 5 = bottom right.

Bring that trophy home! {nation} is depending on you!
Let's start with {nation} vs Germany in a penalty shootout!!!
"""
        print_one_letter_at_a_time(intro_text)

        player_choice = get_heads_or_tails_input("Heads or Tails? \n")
        toss_result = coin_toss()
        print(f"The coin toss result is {toss_result}.\n")

        if player_choice == toss_result:
            print("You won the coin toss! "
                  f"Do you want to take the first penalty? (yes/no): \n")
            if get_yes_no_input("") == "yes":
                first_shooter = "player"
            else:
                first_shooter = "computer"
        else:
            first_shooter = "computer"
            print("Philipp Lahm won the coin toss "
                  f"and will take the first penalty.\n")

        while True:
            player_goals, computer_goals = game(name, nation, first_shooter)
            print("That's all they needed! \n")

            if player_goals > computer_goals:
                print(f"{name} has won it for {nation}! What a legend!")
            else:
                print(f"Germany breaks the hearts of {nation}")

            play_again = get_yes_no_input("Fancy another go? (yes/no): \n")
            if play_again != 'yes':
                break

        print("All the best buddy!")

    else:
        print("Okay then, enjoy your day.")

if __name__ == "__main__":
    main()