import random

print("Welcome to RPS")

user_score = 0
comp_score = 0
ties = 0
name = input("Enter your name here: ")

print("""
      Winning rules:
      1. Paper vs Rock --> Paper
      2. Rock vs Scissors --> Rock
      3. Scissors vs Paper --> Scissors""")

while True:
    choice = int(input("Enter your choice from 1-3: "))
    print()
    
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
    
    user = random.randint(1, 3)
    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "scissors"
    
    print("The user's choice is", user_choice)
    print("Now it's the computer's turn")
    
    computer = random.randint(1, 3)
    if computer == 1:
        comp_choice = "rock"
    elif computer == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"
    
    print("The computer's choice is", comp_choice)
    
    if ((user_choice == "paper" and comp_choice == "rock") or
            (user_choice == "rock" and comp_choice == "paper")):
        print("Paper wins")
        result = "paper"
    elif ((user_choice == "scissors" and comp_choice == "rock") or
            (user_choice == "rock" and comp_choice == "scissors")):
        print("Rock wins")
        result = "rock"
    elif user_choice == comp_choice:
        print("It's a tie")
        result = "tie"
    else:
        print("Scissors win")
        result = "scissors"
    
    if result == "tie":
        ties += 1
    elif result == user_choice:
        user_score += 1
        print("User wins")
    else:
        comp_score += 1
        print("Computer wins")
    
    print("Scores are:")
    print(name, "'s score is", user_score)
    print("Computer's score is", comp_score)
    print("Ties are", ties)
    
    repeat = input("Do you want to play again? (yes/no): ")
    if repeat == "no":
        print("Game is over!")
        break

print("Thanks for playing")
