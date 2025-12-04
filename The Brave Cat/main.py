from art import logo, menu
from character_creation import start_character_creation
from utils import clear_screen

def main():
    clear_screen()
    print(logo)
    print(menu)

    while True:
        choice = input("Choose your fate: ").strip()

        if choice == "1":
            clear_screen()
            print("\n⚔ The cursed path awaits... ⚔\n")
            start_character_creation()
            break

        elif choice == "2":
            print("\n👁 The void consumes the weak. Exiting...\n")
            quit()

        else:
            print("\n❌ Invalid input. The darkness rejects your choice.\n")

if __name__ == "__main__":
    main()
