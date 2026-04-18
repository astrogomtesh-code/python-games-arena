import random

print('-' * 50 + " PYTHON GAMES ARENA " + '-' * 50)


while True:
    print("\n1. Rock Paper Scissors")
    print("2. Guess the Number")
    print("3. Quit")

    try:
        choice = int(input("Enter a number: "))
    except:
        print("Enter a valid number. Not a philosophical concept.")
        continue

    if choice == 1:
        print("\nYou chose Rock Paper Scissors")

        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)

        user = input("\nChoose rock, paper, or scissors: ").lower()

        wins_against = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if user not in choices:
            print("\nInvalid input. Try again without inventing new weapons.")
            continue

        print("\nComputer chose:", computer)

        if user == computer:
            print("\nIt's a tie")
        elif wins_against[user] == computer:
            print("\nYou win")
        else:
            print("\nYou lose")

        print("-" * 120)

    elif choice == 2:
        print("\nYou have entered the number guessing game")

        number = random.randint(0, 10)
        guesses_left = 3

        while guesses_left > 0:
            try:
                user_guess = int(input("\nGuess a number between 0 and 10: "))
            except:
                print("\nEnter a real number, not vibes.")
                continue

            if user_guess == number:
                print("\nCongratulations, you won")
                break
            else:
                print("\nWrong.")
                if user_guess > number:
                    print("\nLower")
                else:
                    print("\nHigher")

                guesses_left -= 1
                print("\nGuesses left:", guesses_left)

        if guesses_left == 0:
            print(f"\nSorry, you lost. The answer was {number}")

        print("-" * 120)

    elif choice == 3:
        print("GG")
        break

    else:
        print("Invalid choice.")
        
        



        
        


        
        



        
        
