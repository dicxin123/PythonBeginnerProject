import random

user_wins = 0   
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, scissors, paper or quit: ").lower()
    
    if user_input == "quit":
        print("Goodbye!")
        print("You have won", user_wins, "times.")
        print("The computer has won", computer_wins, "times.")
        print("Thanks for playing!")
        quit()
        
    if user_input not in options:
        print("Please enter a valid input")
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
            
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
            
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
            
    elif user_input == computer_pick:
        print("It's a tie!")
            
    else:
        print("You lost!")
        computer_wins += 1
              
    print("You have won", user_wins, "times.")
    print("The computer has won", computer_wins, "times.")

    
    