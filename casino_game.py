import random

# virtual casino game

# variables
player_name = input("Enter your name: ")
balance = 1000
games_played = 0
games_won = 0
games_lost = 0

# list
# game histroy store karne ke liye
history = []

# tuple
# fixed game names store karne ke liye
game_names = (
    "Number Guessing Game",
    "Lucky Spin",
    "Rock Paper Scissors"
)

# dictionary
# rock paper scissors choices
choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

print("\n" + "=" * 55)
print("       WELCOME TO VIRTUAL CASINO")
print("=" * 55)

print("Player Name:", player_name)
print("Starting Balance:", balance, "Virtual Coins")

print("\nAvailable Games:")

# tuple ko display karne ke liye loop
for game in game_names:
    print("-", game)


# main loop game

while True:

    # game over condition
    if balance <= 0:
        print("\n" + "=" * 40)
        print("GAME OVER!")
        print("You have no coins left.")
        print("=" * 40)
        break

    print("\n" + "=" * 50)
    print("              MAIN MENU")
    print("=" * 50)

    print("1. Number Guessing Game")
    print("2. Lucky Spin")
    print("3. Rock Paper Scissors")
    print("4. Check Status")
    print("5. View Game History")
    print("6. Get Random Bonus")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    # number guessing game

    if choice == "1":

        print("\n--- NUMBER GUESSING GAME ---")
        print("Guess a number between 1 and 10")
        print("Correct guess = Win 3x your bet")

        bet = int(input("Enter your bet: "))

        if bet <= 0:
            print("Bet must be greater than 0.")

        elif bet > balance:
            print("Insufficient balance!")

        else:

            guess = int(input("Enter your guess (1-10): "))

            if guess < 1 or guess > 10:
                print("Invalid number! Enter between 1 and 10.")

            else:

                computer_number = random.randint(1, 10)

                print("Winning Number:", computer_number)

                games_played += 1

                if guess == computer_number:

                    reward = bet * 3
                    balance += reward
                    games_won += 1

                    print("\nJACKPOT!")
                    print("You won", reward, "coins!")

                    # list mein history add
                    history.append(
                        "Number Guessing - WON " + str(reward) + " coins"
                    )

                else:

                    balance -= bet
                    games_lost += 1

                    print("\nYou lost", bet, "coins.")

                    history.append(
                        "Number Guessing - LOST " + str(bet) + " coins"
                    )

    # lucky spin

    elif choice == "2":

        print("\n--- LUCKY SPIN ---")
        print("Possible Results: 0x, 1x, 2x, 5x")

        bet = int(input("Enter your bet: "))

        if bet <= 0:
            print("Bet must be greater than 0.")

        elif bet > balance:
            print("Insufficient balance!")

        else:

            # LIST
            multipliers = [0, 1, 2, 5]

            result = random.choice(multipliers)

            print("\nSpin Result:", result, "x")

            games_played += 1

            if result == 0:

                balance -= bet
                games_lost += 1

                print("You lost", bet, "coins.")

                history.append(
                    "Lucky Spin - LOST " + str(bet) + " coins"
                )

            elif result == 1:

                print("Draw! You got your bet back.")

                history.append(
                    "Lucky Spin - DRAW"
                )

            else:

                reward = bet * result
                balance += reward
                games_won += 1

                print("Congratulations!")
                print("You won", reward, "coins!")

                history.append(
                    "Lucky Spin - WON " + str(reward) + " coins"
                )

    # rock paper scissor

    elif choice == "3":

        print("\n--- ROCK PAPER SCISSORS ---")

        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        bet = int(input("Enter your bet: "))

        if bet <= 0:
            print("Bet must be greater than 0.")

        elif bet > balance:
            print("Insufficient balance!")

        else:

            player_choice = int(input("Choose 1-3: "))

            if player_choice < 1 or player_choice > 3:
                print("Invalid choice!")

            else:

                computer_choice = random.randint(1, 3)

                print("\nYou chose:", choices[player_choice])
                print("Computer chose:", choices[computer_choice])

                games_played += 1

                if player_choice == computer_choice:

                    print("DRAW!")

                    history.append(
                        "Rock Paper Scissors - DRAW"
                    )

                elif (
                    (player_choice == 1 and computer_choice == 3)
                    or
                    (player_choice == 2 and computer_choice == 1)
                    or
                    (player_choice == 3 and computer_choice == 2)
                ):

                    reward = bet * 2
                    balance += reward
                    games_won += 1

                    print("YOU WON!")
                    print("You won", reward, "coins!")

                    history.append(
                        "Rock Paper Scissors - WON " +
                        str(reward) + " coins"
                    )

                else:

                    balance -= bet
                    games_lost += 1

                    print("YOU LOST!")
                    print("You lost", bet, "coins.")

                    history.append(
                        "Rock Paper Scissors - LOST " +
                        str(bet) + " coins"
                    )

    # check status

    elif choice == "4":

        print("\n" + "=" * 40)
        print("         PLAYER STATUS")
        print("=" * 40)

        print("Player:", player_name)
        print("Balance:", balance, "coins")
        print("Games Played:", games_played)
        print("Games Won:", games_won)
        print("Games Lost:", games_lost)

        if games_played > 0:

            win_percentage = (
                games_won / games_played
            ) * 100

            print(
                "Win Percentage:",
                round(win_percentage, 2),
                "%"
            )

        else:
            print("Win Percentage: No games played")

    # game history

    elif choice == "5":

        print("\n--- GAME HISTORY ---")

        if len(history) == 0:
            print("No games played yet.")

        else:

            count = 1

            for game in history:

                print(
                    str(count) + ".",
                    game
                )

                count += 1

    # random bonus

    elif choice == "6":

        bonus = random.randint(50, 200)

        balance += bonus

        print("\nBONUS!")
        print("You received", bonus, "coins!")

        history.append(
            "Bonus Received - " +
            str(bonus) + " coins"
        )
    # exit

    elif choice == "7":

        print("\n" + "=" * 50)
        print("THANK YOU FOR PLAYING,", player_name)
        print("Final Balance:", balance, "coins")
        print("Total Games Played:", games_played)
        print("=" * 50)

        break

    # invalid choice

    else:

        print("Invalid choice! Please enter 1 to 7.")
