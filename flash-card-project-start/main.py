BACKGROUND_COLOR = "#B1DDC6"


# import modules
import tkinter as tk
import pandas as pd
import random



#global dictionaries
to_learn = {} #contains words yet to learn once ticked right, they'llbe removed from this dictionary
curr_card = {} #random card from to_learn dictionary


# import to_learn from words to learn csv, if not found then import from original
try:
    df = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_df = pd.read_csv('./data/french_words.csv')
    to_learn = original_df.to_dict(orient ="records")
else:
    to_learn = df.to_dict(orient ="records")


#functions
def next_card():
    global curr_card
    global flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title,text = "French", fill = "black")
    canvas.itemconfig(card_word, text = curr_card["French"], fill = "black")
    flip_timer= window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image = card_back)
    canvas.itemconfig(card_title,text = "English", fill = "white")
    canvas.itemconfig(card_word, text= curr_card["English"], fill="white")



def right():
    to_learn.remove(curr_card)
    print(len(to_learn))
    new_df = pd.DataFrame(to_learn)
    new_df.to_csv('./data/words_to_learn.csv', index = False)
    next_card()



# ------------------ui setup------------------------------------------------------------#
window = tk.Tk();
window.title("Flashy - A Simple Flashcard App")
window.config(bg= BACKGROUND_COLOR, pady=50, padx = 50)
flip_timer = window.after(3000, func = flip_card)
#setup canvas images
canvas = tk.Canvas(width= 800, height = 526 )
card_front = tk.PhotoImage(file = './images/card_front.png')
card_back = tk.PhotoImage(file = './images/card_back.png')

canvas_image = canvas.create_image(400,270, image = card_front)

#canvas content
card_title = canvas.create_text(400,150,text="title", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="word",  font = ("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column= 0, columnspan=2)

#buttons
right_image = tk.PhotoImage(file = "./images/right.png")
right_button = tk.Button(image = right_image, highlightthickness=0, borderwidth=0, command = right)
right_button.grid(row = 1,column=1)

wrong_image = tk.PhotoImage(file = "./images/wrong.png")
wrong_button = tk.Button(image = wrong_image, highlightthickness=0, borderwidth=0 , command = next_card())
wrong_button.grid(row = 1,column=0)




window.mainloop()