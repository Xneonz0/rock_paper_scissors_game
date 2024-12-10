def rock_paper():
    import random

    choices = ('r', 'p', 's')
    emoji={"r":'🪨',"s":'✂️',"p":'📄'}  #emojies

    print("Welcome to rock, paper, scissors game!")
    print("In order to win, you must beat the computer in best of 3 rounds!")
    print("Good luck\n")

    while True:
        player_score = 0
        computer_score = 0
        current_round = 1
        rounds = 3

        while current_round <= rounds:  # round system
            print(f"Current round is {current_round} of {rounds}\n")

            user_choice = input("Please enter your choice! (r/p/s): ").strip().lower()  # user input checker
            if user_choice not in choices:
                print("Invalid choice!\n")
                continue

            computer_choice = random.choice(choices)  

            print(f"Your choice is: {emoji[user_choice]}")  # display choices
            print(f"Computer's choice is: {emoji[computer_choice]}")

            if user_choice == computer_choice:
                print("It's a draw!\n")
            elif (
                (user_choice == 'r' and computer_choice == 's') or
                (user_choice == 'p' and computer_choice == 'r') or
                (user_choice == 's' and computer_choice == 'p')
            ):
                print("You won!\n")
                player_score += 1
            else:
                print("You lost!\n")
                computer_score += 1

            current_round += 1

            if player_score == 3 or computer_score == 3: #breaks the inner loop that tracks rounds
                break

        if player_score > computer_score: #determine who wins
            print("You won the game!\n")
        elif player_score < computer_score:
            print("You lost the game!\n")
        else:
            print("It's a draw!\n")

        print(f"Your score is: {player_score}")
        print(f"The computer's score is: {computer_score}")
        print("Thank you for playing!\n")

        while True:
            should_continue = input("Would you like to play another game? (yes/no): ").lower().strip()  # check if user wants to continue
            if should_continue in ['yes', 'y']:
                break  
            elif should_continue in ['no', 'n']:
                print("Exiting game...")
                return
            else:
                print("Invalid choice! Enter a valid choice!")

rock_paper()
