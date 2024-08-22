import random
possible_action = ["rock", "paper", "scissor"]
while True:
    user_choice = input("Enter your choice(rock, paper, or scissor): ").lower()
    computer_choice = random.choice(possible_action).lower()
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie")
    elif user_choice == "rock" and computer_choice == "scissor":
        print("Rock beats scissor. You Win!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("Paper cover rock. You Loss!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("Paper beats rock. You Win!")
    elif user_choice == "scissor" and computer_choice == "rock":
        print("Rock beats scissor. You Loss!")
    elif user_choice == "scissor" and computer_choice == "paper":
        print("Scissor cut paper. You Win!")
    elif user_choice == "paper" and computer_choice == "scissor":
        print("Scissor cut paper. You Loss!")
    else:
        print("Invalid input, Please enter rock, paper, or scissor.")
    play_again = input("\nWould you like to play again? (y/n): ")
    if play_again == "y":
        continue
    else:
        break