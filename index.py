import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected. Please enable at least one character type.")

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("<----------- Random Password Generator ----------->\n")
    
    length = 0
    use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    while True:
        if length == 0:
            try:
                length = int(input("Enter the desired length of the password: "))
                if length <= 0:
                    print("Password length must be a positive number.")
                    continue
            except ValueError:
                print("Invalid length. Please enter a valid number.")
                continue

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password is: {password}\n")

        generate_another = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if generate_another == 'yes':
            change = input("Do you want to change the character types or length? (yes/no): ").strip().lower()
            if change == 'yes':
                length_change = input("Do you want to change the password length? (yes/no): ").strip().lower()
                if length_change == 'yes':
                    try:
                        length = int(input("Enter the new desired length of the password: "))
                        if length <= 0:
                            print("Password length must be a positive number.")
                            continue
                    except ValueError:
                        print("Invalid length. Please enter a valid number.")
                        continue

                use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
                use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
                use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        else:
            print("\nExiting the Password Generator. Have a great day!")
            break

if __name__ == "__main__":
    main()
