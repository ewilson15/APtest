import random

def RPC():
    choices = ['rock', 'paper', 'scissors', 'dirt']
    computer_choice = random.choice(choices)
    print("Note that choosing dirt will give a 50% chance of victory.")
    user_choice = input("Enter your choice of rock, paper, scissors, or dirt: ").lower()

    print("Your opponent chose:", computer_choice)

    if user_choice not in choices:
        print("Invalid choice. Please choose again from rock, paper, scissors, or dirt.")
        return

    if user_choice == computer_choice:
        print("Tie!")

    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win!")
        elif computer_choice == 'dirt':
            if random.random() < 0.5:
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You lose!")

    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("You win!")
        elif computer_choice == 'dirt':
            if random.random() < 0.5:
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You lose!")

    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("You win!")
        elif computer_choice == 'dirt':
            if random.random() < 0.5:
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You lose!")

    elif user_choice == 'dirt':
        if random.random() < 0.5:
            print("You win! The luck of dirt was on your side.")
        else:
            print("You lose! The luck of dirt was not on your side.")

RPC()