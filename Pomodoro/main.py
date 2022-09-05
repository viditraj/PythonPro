import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def reset_timer():
    window.after_cancel(time)
    title_label.config(text="Timer")
    canvas.itemconfig(timer, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown_timer(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown_timer(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown_timer(work_sec)


def countdown_timer(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = math.floor(count % 60)
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, countdown_timer, count - 1)
    else:
        mark = ""
        work_reps = math.floor(reps / 2)
        for _ in range(work_reps):
            mark += "✔"
        check_label.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(width=200, height=224, bg=YELLOW)
window.config(padx=100, pady=50)
title_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 42, "bold"), fg=GREEN)
title_label.grid(column=2, row=0)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)

start_button = Button(text="Start", relief=FLAT, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=1, row=3)

check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=2, row=4)

reset_button = Button(text="Reset", relief=FLAT, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()
