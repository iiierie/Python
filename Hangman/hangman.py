import random
from hangman_words import word_list
import hangman_arts as h_arts
end_of_game = False
life = 6
print(h_arts.welcome)
print(h_arts.logo)

chosen_word = random.choice(word_list)
length = len(chosen_word)

# create display list[_ , _ , _ , _]
display = []
for _ in range(length):
    display += "_"

while not end_of_game:
    guess = input("Enter your guess letter: ")

    if guess in display:
        print("You have already guessed this letter bruh!")

    for i in range(length): #CORRECT GUESS SO DISPLAY THAT LETTER IN THE RESPECTIVE POSITION
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word: #wrong guess
        life-=1;
        print("\nOops. It's not a right guess! You lose a life. Remaining chances:{} ".format(life))
        if life == 0:
            end_of_game = True
            print("You lose lol.")
        print(h_arts.stages[life])

    if "_" not in display:
            end_of_game = True
            print("You won! Congrats ")

    if life == 0 and "_" in display:
        print("The actual word was {}.".format(chosen_word.upper()))
    else:
        print(f"{' '.join(display)}")


''' 
simple to understand flow of the program:

step 1: computer randomly selects a word from the wordlist and creates equal number of _ blank spaces to print on screen
step 2: loop until game ends when user wins i.e. no _ available in the display list OR when user loses i.e. 0 lives left
        - if guess letter is already guessed once print already guessed
        - if guess letter is not in the word then lose a life,print hangman accordingly and check if life is 0, if yes then game lose 
        - if guess letter is in the word then display the letter in the same position 
        - finally check if all letters are guessed correctly i.e no "_" in the display list , so game win

'''