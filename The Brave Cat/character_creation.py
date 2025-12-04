from art import who_are_you, char_options
from utils import clear_screen

def start_character_creation():
    clear_screen()
    print(who_are_you)
    print(char_options)

    choice = input("Choose an option: ").strip()

    if choice == "1":
        custom_character()
    elif choice == "2":
        origin_character()
    else:
        print("Invalid choice... try again.")
        start_character_creation()

def custom_character():
    clear_screen()
    print("🛠 Custom character creator loading... (later)\n")

def origin_character():
    clear_screen()
    print("📜 Origin selection loading... (later)\n")
