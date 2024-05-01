#Task 4 - Rock , paper , scissors Game


import random

def get_user_choice():
    while True:
        user_choice = input("Please choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return f"{user_name.capitalize()} wins!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    
    print("Welcome to the Rock-Paper-Scissors Game!\n")
    
    while True:
        print("New round!\n")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == f"{user_name.capitalize()} wins!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"\nScore - You: {user_score}, Computer: {computer_score}\n")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nThank you for playing, {user_name}!")
            break

# Ask for the user's name
user_name = input("Enter your name: ")
play_game()

'''
OUTPUT : 
Enter your name: Miya
Welcome to the Rock-Paper-Scissors Game!

New round!

Please choose rock, paper, or scissors: rock

You chose: rock
Computer chose: paper
Computer wins!

Score - You: 0, Computer: 1

Do you want to play again? (yes/no): yes
New round!

Please choose rock, paper, or scissors: paper

You chose: paper
Computer chose: rock
Miya wins!

Score - You: 1, Computer: 1

Do you want to play again? (yes/no): yes
New round!

Please choose rock, paper, or scissors: rock

You chose: rock
Computer chose: paper
Computer wins!

Score - You: 1, Computer: 2

Do you want to play again? (yes/no): no

Thank you for playing, Miya!
'''
