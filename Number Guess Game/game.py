from art import logo
import random


lives = 10
end_game = False


def get_a_number():
    return random.randint(1, 101)


def check_number(actual_number, user_number):
    global lives
    global end_game
    lives -= 1
    if actual_number == user_number:
        end_game = True
        return "Bingo! You got the right number. "

    if lives == 0:
        end_game = True
        return (f"You lose. You lost all lives. The actual number was {actual_number}. ")
    else:
        if actual_number < user_number:
            return f"Too high! \nTry again. You still have {lives} lives remaining."
        else:
            return f"Too low! \nTry again. You still have {lives} lives remaining."


def input_number():
    number = int(input("Make a guess: "))
    return number


def play_game():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

    actual_number = get_a_number()

    diff = input("Choose a difficulty mode: Easy or Hard? ")
    if diff.upper() == "HARD":
        global lives
        lives -= 5
    print(f"Alrighty! You have total of {lives} attempts remaining to correctly guess the number.")

    while not end_game:
        user_number = input_number()
        print(check_number(actual_number, user_number))


def main():
    print(logo)
    play_game()
    if input("Want to play again? Y/N").upper() == "Y":

        play_game()
    print("BYEBYE!")


main()