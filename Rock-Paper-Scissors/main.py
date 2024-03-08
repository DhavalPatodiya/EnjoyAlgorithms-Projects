# A small game for Rock-Paper-Scissor
import random

possiblities = ['Rock', 'Paper', 'Scissor']
score = 0
player_score = 0

while score != 3 and player_score != 3:
    system_choice = (random.choice(possiblities)).lower()
    
    print("Choose any one from below choices:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    player_choice = (str(input())).lower()

    if system_choice == "paper":
        if player_choice == "scissor":
            player_score += 1
        elif player_choice == "rock":
            score += 1
    elif system_choice == "rock":
        if player_choice == "scissor":
            score += 1
        elif player_choice == "paper":
            player_score += 1
    elif system_choice == "scissor":
        if player_choice == "paper":
            score += 1
        elif player_choice == "rock":
            player_score += 1

    print(f'\nSystem choice: {system_choice}, Player choice: {player_choice}')
    print(f'Player score: {player_score}, System score: {score}\n')


if score == 3:
    print("Winner: System")
else:
    print("Winner: Player")
