from tkinter import *
import pandas
from random import choice
from tkinter import messagebox
import csv

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(pady=50, padx=20, bg=BACKGROUND_COLOR)
# ----choose a random word --- #


try:
    words_data = pandas.read_csv('./data/words_to_learn.csv').to_dict(orient="records")
except FileNotFoundError:
    words_data = pandas.read_csv('./data/deck_english.csv').to_dict(orient="records")

word_chosen = {}


def words_to_learn():
    index = words_data.index(word_chosen)
    words_data.pop(index)
    file = pandas.DataFrame(words_data)
    file.to_csv('./data/words_to_learn.csv')
    if len(words_data) == 0:
        messagebox.showinfo(title='congratulation', message='You learn all the words')


def next_card():
    global word_chosen, flip_timer
    window.after_cancel(flip_timer)
    word_chosen = choice(words_data)
    canvas.itemconfig(title, text='English')
    canvas.itemconfig(card_background, image=front_photo)
    canvas.itemconfig(target_language, text=word_chosen['english'])
    window.after(3000, retro)


# # ------ Retro------#
def retro():
    canvas.itemconfig(card_background, image=back_photo)
    canvas.itemconfig(title, text='Spanish')
    canvas.itemconfig(target_language, text=word_chosen['spanish'])


# ------ UI interface ------#

# canvas
flip_timer = window.after(3000, retro)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
front_photo = PhotoImage(file='./images/card_front.png')
back_photo = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 526 / 2, image=front_photo)
title = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
target_language = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))

# buttons
img_right = PhotoImage(file='./images/right.png')
btn_right = Button(image=img_right, highlightthickness=0, borderwidth=0, pady=50,
                   command=lambda: [next_card(), words_to_learn()])
btn_right.grid(column=1, row=1)

img_wrong = PhotoImage(file='./images/wrong.png')
btn_wrong = Button(image=img_wrong, highlightthickness=0, borderwidth=0, pady=50, command=next_card)
btn_wrong.grid(column=0, row=1)

next_card()
window.mainloop()
