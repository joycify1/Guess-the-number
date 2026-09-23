import random

def play_game():
    lucky_num = random.randint(1, 50)
    while True:
        user_num = int(input("Guess the lucky number: "))
        if user_num == lucky_num:
            print("Huraaaay. You won! Game over.")
            break
        elif user_num < lucky_num:
            print("Too low, oops!")
        else:
            print("Too high, try again!")
    print("Thanks for playing, hope you had fun.")

play_game()
