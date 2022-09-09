import time
from tkinter import *
import pandas
import random
from progress import *

BACKGROUND_COLOR = "#B1DDC6"
counts = 0

# data = pandas.read_csv("./data/french_words.csv")

to_learn = words_to_learn()

card = {}


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_text, text=card["English"], fill="White")


def next_card():
    global card, card_timer
    window.after_cancel(card_timer)
    card = random.choice(to_learn)
    new_card = card["French"]
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_text, text=f"{new_card}", fill="Black")
    card_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(card)
    save_progress(to_learn)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_timer = window.after(3000, next_card)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, relief=FLAT, command=next_card)
cross_button.grid(column=0, row=1)

tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, borderwidth=0, relief=FLAT, command=is_known)
tick_button.grid(column=1, row=1)

next_card()

window.mainloop()
