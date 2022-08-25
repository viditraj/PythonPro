import random
from art import rock, paper, scissors

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_input < 0 or user_input > 2:
    print("You choose invalid number!You Lose")
else:
    choices = [rock, paper, scissors]
    computer_choice = random.choice(choices)
    user_choice = choices[user_input]
    computer_input = choices.index(computer_choice)
    outcomes = ["You Won", "You Lose", "Its A Draw"]
    result = ""
    if computer_input == 0:
        if user_input == 1:
            result = outcomes[0]
        elif user_input == 2:
            result = outcomes[1]
        else:
            result = outcomes[2]
    elif computer_input == 1:
        if user_input == 0:
            result = outcomes[1]
        elif user_input == 2:
            result = outcomes[0]
        else:
            result = outcomes[2]
    elif computer_input == 2:
        if user_input == 0:
            result = outcomes[0]
        elif user_input == 1:
            result = outcomes[1]
        else:
            result = outcomes[2]
    print("Computer's choice :\n")
    print(choices[computer_input])
    print("Your choice :\n")
    print(choices[user_input])
    print(result)

