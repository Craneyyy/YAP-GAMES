import random
import time as t
import sys

def loading():
    spinner = ['|', '/', '-', '\\']
    for i in range(10):
        sys.stdout.write('\rLoading [' + spinner[i % len(spinner)] + ']')
        sys.stdout.flush()
        t.sleep(0.3)
    
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()
def game_load():
    spinner = ['|', '/', '-', '\\']
    for i in range(5):
        sys.stdout.write('\rLoading [' + spinner[i % len(spinner)] + ']')
        sys.stdout.flush()
        t.sleep(0.3)
    
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()


def guess_Game():
    print("Guess a number from 1, 10: ")
    num = random.randint(1, 10)
    try:
        ans = int(input("Your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if (num != ans):
        print(f"Wrong the answer was {num}")
    else:
        print(f"you guessed right, the answer is {num}")


def valid_input(inp):
    if inp == "paper" or inp == "rock" or inp == "scissors":
        return True
    else:
        return False

def rps():
    pick = ["rock", "paper", "scissors"]
    bot = random.choice(pick)
    print("Play a game of rock, paper and, scissors")
    player_1 = str(input("Your move: ").strip().lower())

    if valid_input(bot) and valid_input(player_1):
        if bot == player_1:
            print(f"Player 1 choice: {player_1}, Bot's choice: {bot}")
            print("It's a tie!")
        elif (player_1 == "paper" and bot == "rock") or\
             (player_1 == "rock" and bot == "scissors") or\
             (player_1 == "scissors" and bot == "paper"):
            print("You win")
        else:
            print(f"Player 1 choice: {player_1}, Bot's choice: {bot}")
            print("Bot win's")
            
    else:
        print("Invalid input - must be 'paper', 'rock', or 'scissors' ")

def main():
    loading()
    print("\n")
    while True:
        print("--------- Game's ---------")
        print("| Choose a game to play. |")
        print("| 1 = Guess a Number     |")
        print("| 2 = Rps                |")
        print("| 3 = Exit Program       |")
        print("--------------------------")
        try:  
            choice =  int(input("Input choice: ").strip())  
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            game_load()
            guess_Game()
            game_load()
        elif choice == 2:
            game_load()
            rps()
            game_load()
        elif choice == 3:
            print("Exiting program....")
            t.sleep(0.3)
            break
        else:
            print("Invalid choice try again.")

main()
