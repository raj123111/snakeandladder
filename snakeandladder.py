
import random

def snakeladdergame():
    n = int(input("Enter how many players want to play: "))
    if n <= 0:
        print("Invalid number of players. Please enter a positive number.")
        return

    players = {}
    for i in range(n):
        player = input(f"Enter player {i+1}'s name: ")
        players[player] = 0

    snakes = {17: 7, 54: 34, 62: 19, 98: 79}
    ladders = {3: 38, 24: 33, 42: 93, 72: 84}

    current_player_index = 0
    while True:
        current_player = list(players.keys())[current_player_index]
        input(f"{current_player}'s turn. Press Enter to roll the dice.")
        dice_roll = random.randint(1, 6)
        print(f"{current_player} rolled a {dice_roll}")
        players[current_player] += dice_roll

        if players[current_player] > 100:
            players[current_player] -= dice_roll
            print(f"{current_player} is at position {players[current_player]}.")
            continue

        if players[current_player] in snakes:
            print(f"{current_player} landed on a snake at {players[current_player]}.")
            players[current_player] = snakes[players[current_player]]
            print(f"{current_player} slid down to {players[current_player]}.")

        elif players[current_player] in ladders:
            print(f"{current_player} landed on a ladder at {players[current_player]}.")
            players[current_player] = ladders[players[current_player]]
            print(f"{current_player} climbed up to {players[current_player]}.")

        print(f"{current_player} is at position {players[current_player]}.")

        if players[current_player] == 100:
            print(f"\nCongratulations! {current_player} wins!")
            break

        current_player_index = (current_player_index + 1) % n
snakeladdergame()
