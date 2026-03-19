import random

options = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0

print("Welcome to Rock, Paper, Scissors!\n")

while True:   
    player_choice = input("Enter a choice (Rock, Paper, Scissors) or '`' to quit: ").lower()
    if player_choice == '`':
        break
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(options)
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a Draw!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print(f"{player_choice.capitalize()} beats {computer_choice}. You win!")
        player_wins += 1
    else:
        print(f"{computer_choice.capitalize()} beats {player_choice}. Computer wins!")
        computer_wins += 1
    
    
    print(f"Score: Player {player_wins} - Computer {computer_wins}\n")

print("\nGAME OVER!")
print(f"Final Score: Player {player_wins} - Computer {computer_wins}")
