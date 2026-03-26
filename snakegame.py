
snakes = {
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
    64: 60, 87: 24, 93: 73, 95: 75, 98: 78
}

ladders = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84,
    36: 44, 51: 67, 71: 91, 80: 100
}

player1 = 0
player2 = 0

print("🐍 Snake and Ladder Game 🪜 (2 Players)")

while True:

    while True:
        dice = int(input("\nPlayer 1 - Enter dice number (1-6): "))

        if dice < 1 or dice > 6:
            print("❌ Invalid dice number!")
            continue

        if player1 + dice <= 100:
            player1 += dice

            if player1 in snakes:
                print("🐍 Snake Bite!")
                player1 = snakes[player1]

            elif player1 in ladders:
                print("🪜 Ladder! Climb up!")
                player1 = ladders[player1]

        print("Player 1 position:", player1)

        if player1 == 100:
            print("🎉 Player 1 Wins!")
            exit()

        # Extra turn if dice = 6
        if dice != 6:
            break
        else:
            print("🎲 Got 6! Roll again.")

    while True:
        dice = int(input("\nPlayer 2 - Enter dice number (1-6): "))

        if dice < 1 or dice > 6:
            print("❌ Invalid dice number!")
            continue

        if player2 + dice <= 100:
            player2 += dice

            if player2 in snakes:
                print("🐍 Snake Bite!")
                player2 = snakes[player2]

            elif player2 in ladders:
                print("🪜 Ladder! Climb up!")
                player2 = ladders[player2]

        print("Player 2 position:", player2)

        if player2 == 100:
            print("🎉 Player 2 Wins!")
            exit()

        if dice != 6:
            break
        else:
            print("🎲 Got 6! Roll again.")