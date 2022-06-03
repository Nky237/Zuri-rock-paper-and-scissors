import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player= input("Is it 'rock', 'paper' or 'scissors': ").lower()

# for the tie
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("it is a tie!")


    elif player == 'rock':
   # for loosing
        if computer == 'paper':
            print("computer: ", computer)
            print("player: ", player)
            print("You lost!")
# For winning
        if computer == 'scissors':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")


    elif player == 'scissors':
# for loosing
        if computer == 'rock':
            print("computer: ", computer)
            print("player: ", player)
            print("You lost!")
# For winning
        if computer == 'paper':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")


    elif player == 'paper':
    # for loosing
        if computer == 'scissors':
            print("computer: ", computer)
            print("player: ", player)
            print("You lost!")
# For winning
        if computer == 'rock':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    play_again = input("Do you want to play again? 'yes' or 'No':  ").lower()
    if play_again != 'yes':
        break
print("Bye")