import random

#change to sword, gun, shield, hammer

def RPC():
    choices = ['rock', 'paper', 'scissors', 'dirt']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors, or dirt): ").lower()

    print("Your opponent chose:", computer_choice)

    if user_choice not in choices:
        print("Invalid choice. Please choose again from rock, paper, scissors, or dirt.")
        return

    if user_choice == computer_choice:
        print("Draw!")

    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win!")
        elif computer_choice == 'dirt':
            if random.random() < 0.5:
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You lose! Bitch")

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
        if computer_choice == 'rock' or computer_choice == 'scissors':
            print("You win!")
        else:
            print("You lose!")

RPC()