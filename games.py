
import random

print('-' * 50 + " PYTHON GAMES ARENA " + '-' * 50)


while True:
    print("\n1. Rock Paper Scissors")
    print("\n2. Guess the Number")
    print("\n3.quit")

    choice = int(input("Enter a number: "))

    if choice == 1:
        print("You chose Rock Paper Scissors")

        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)

        user = input("Choose rock, paper, or scissors: ").lower()

        wins_against = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if user not in choices:
            print("Invalid input. Try again without inventing new weapons.")
            continue

        print("Computer chose:", computer)

        if user == computer:
            print("It's a tie")
        elif wins_against[user] == computer:
            print("You win")
        else:
            print("You lose")
            
        print("-" * 120)
    
    elif choice == 2:

        guess = 3
        number = random.randint(0,10)
        print("You have entered the number guessing game")
        while True:
           user_guess = int(input("guess a numer between 0 and 10 : "))
           if user_guess == number:
               print (" Congratulations you won ")
               break
           elif user_guess != number:
               print("sorry not it try again")
               guess -= 1
               print("guesses left " ,guess)
               if guess == 0:
                   print(f"Sorry You Lost. The answer was {number}")
                   print("-" * 120)
                   break
    elif choice == 3:
        print("GG")
        break

        
        



        
        
