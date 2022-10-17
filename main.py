BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pandas
import random

current_card = {}
to_learn = {}

try:
    data_words = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data_words.to_dict(orient='records')



def pick_new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(front_card, image=logo_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(front_card, image=back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    pick_new_word()




window = Tk()
window.title('Flashy')
window.config(padx=50, pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
logo_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')

front_card = canvas.create_image(400, 263, image=logo_img)

card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 300, text="", font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

button_img_wrong = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=button_img_wrong, highlightthickness=0, command=pick_new_word)
button_wrong.grid(row=1, column=0)
button_img_right = PhotoImage(file='images/right.png')
button_right = Button(image=button_img_right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

pick_new_word()



window.mainloop()
