import random
import string

print("=" * 45)
print("     RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("\nEnter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        # Ensure at least one of each required character type
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        all_characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        random.shuffle(password)

        print("\nGenerated Password:")
        print("".join(password))

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("\nThank You for using Random Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")
