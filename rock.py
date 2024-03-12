import random

def play_game():
    choices = ['rock', 'paper', 'scissors', 'dirt']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors, or dirt): ").lower()

    print("Computer chose:", computer_choice)

    if user_choice not in choices:
        print("Invalid choice. Please choose from rock, paper, scissors, or dirt.")
        return

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win!")
        elif computer_choice == 'dirt':
            print("You have a 50% chance of winning!")
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
            print("You have a 50% chance of winning!")
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
            print("You have a 50% chance of winning!")
            if random.random() < 0.5:
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You lose!")
    elif user_choice == 'dirt':
        if computer_choice == 'rock' or computer_choice == 'scissors':
            print("You win!")
        else:
            print("You lose!")

play_game()