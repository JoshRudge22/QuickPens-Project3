import random
import time

def print_one_letter_at_a_time(text):
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

def main():
    print_one_letter_at_a_time(ascii_art)
    if get_yes_no_input("Can you step up? (yes/no): \n") == 'yes':
        try:
            name = input("Please enter your name: \n").strip()
            while not name:
                print("Name cannot be empty. Please enter a valid name.")
                name = input("Please enter your name: \n").strip()

            nationality = input(f"Please can {name} enter the country they represent: \n").strip()
            while not nationality:
                print("Country cannot be empty. Please enter a valid country.")
                nationality = input(f"Please can {name} enter the country they represent: \n").strip()

            print(f"We have {name} from {nationality}\n")
            print("""
            Aim is to pick a number different to the computer in order to score.
            If you and the computer both have the same number, the computer makes the save.
            If you and the computer both pick different numbers, then you score.
            Example: if you type 2 and the computer types 3, you've scored a goal. 
            However, if you type 1 and the computer types 1, then the computer makes the save.
            You can go 1 = top left, 2 = bottom left, 3 = middle, 4 = top right, and 5 = bottom right.
            Please don't let your country down. Don't be a Harry Kane!
            Let's start with {nationality} vs Germany in a penalty shootout!!!
            """)

            while True:
                player_goals, computer_saves = game(name)
                print("That's all they needed! \n")
                
                if player_goals >= 3:
                    print(f"{name} has won it for {nationality} what a legend")
                else:
                    print(f"Computer breaks the hearts of {nationality}")

                play_again = get_yes_no_input("Fancy another go? (yes/no): \n")
                if play_again != 'yes':
                    break
            
            print("All the best buddy!")

        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
    else:
        print("Okay then, enjoy your day.")

if __name__ == "__main__":
    main()