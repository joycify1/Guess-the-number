import random

def play_game():
    lucky_num = random.randint(1, 50)       # secret number from 1 to 50
    guesses = 0                             # count valid guesses

    while True:
        try:
            user_num = int(input("Guess the lucky number: "))  # crashes on letters without try/except
        except ValueError:
            print("Please enter a valid number.")
            continue                        # ask again, don't count this guess

        if user_num < 1 or user_num > 50:   # range check
            print("Number must be between 1 and 50.")
            continue                        # out of range, don't count it

        guesses += 1                        # only valid guesses are counted

        if user_num == lucky_num:
            print(f"Huraaaay. You won in {guesses} guesses! Game over.")
            break                           # stop the loop on a win
        elif user_num < lucky_num:
            print("Too low, oops!")
        else:
            print("Too high, try again!")

    print("Thanks for playing, hope you had fun.")

play_game()

