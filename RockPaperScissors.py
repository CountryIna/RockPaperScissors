# Determines the computer's random choice
import random

# Game title with ANSI styling
print("\033[4;30;46m == ROCK PAPER SCISSORS == \033[0m")
print("Type 'EXIT' to stop playing")

choices = {"paper" : "📄", "scissors": "✂️", "rock": "⚫"}
computer_option = list(choices.keys())

while True:
    print("=" *20)
    # User Input
    # Use .lower() to change all letters in the text to lowercase
    user_choice = input("Rock/Paper/Scissors : ").lower()

    # Exit condition
    if user_choice == 'exit':
        print("\nThanks for playing")
        break

    # Validation
    if user_choice not in choices:
        print("⚠️Invalid input. Please type Rock, Paper, Scissors")
        continue
    else:
        # Computer makes a choice
        computer_choice = random.choice(computer_option)

        # Get emojis for display
        user_emoji = choices[user_choice]
        computer_emoji = choices[computer_choice]
        print(f"You chose : {user_choice} {user_emoji}")
        print(f"Computer chose : {computer_choice} {computer_emoji}")

    # Game Logic
    if user_choice == computer_choice:
        result = "\033[1;97;40m DRAW \033[0m"

    elif (user_choice == "scissors" and computer_choice == "paper")or \
            (user_choice == "paper" and computer_choice == "rock")or \
            (user_choice == "rock" and computer_choice == "scissors"):
        result = "\033[1;97;44m 🏆 YOU WIN \033[0m"

    else:
        result = "\033[1;97;41m 😭 YOU LOSE \033[0m"

    # Result
    print("\n == Result ==")
    print(f"{user_emoji} VS {computer_emoji} = {result}")