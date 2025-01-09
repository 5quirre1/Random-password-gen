import string
import random

def get_password_length():
    while True:
        try:
            return int(input("Enter password length: "))
        except ValueError:
            print("Plz enter a number :3")

def get_character_set():
    options = {
        1: string.ascii_letters,
        2: string.digits,
        3: string.punctuation
    }

    print("""Choose character set for password from these: 
        1. Letters
        2. Digits
        3. Special characters
        4. Done (Finish selection)""")

    character_set = ""

    while True:
        try:
            choice = int(input("Pick a number: "))
            if choice in options:
                character_set += options[choice]
                print("Characters added !")
            elif choice == 4:
                if character_set:
                    return character_set
                else:
                    print("Plz select at least one option")
            else:
                print("that's not a choice LOL")
        except ValueError:
            print("only numbers greg")

def generate_password(length, character_set):
    return ''.join(random.choices(character_set, k=length))

def main():
    length = get_password_length()
    character_set = get_character_set()
    password = generate_password(length, character_set)
    print("The random password is:", password)
    print("WARNING, THIS IS JUST FOR FUN, I WOULD NOT RECOMEND USING THIS PASSWORD FOR ANY SENSITIVE DATA LOL\n\n")
    while True:
        choice = input("Do you want to generate another password? (yes/no): ").lower()
        if choice == "yes":
            password = generate_password(length, character_set)
            print("The random password is:", password)
        elif choice == "no":
            print("Bai Bai!")
            break
        else:
            print("hreh")

if __name__ == "__main__":
    main()



# I stole a bit from https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/  <3
