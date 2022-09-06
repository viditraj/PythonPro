from tkinter import *
from tkinter import messagebox
from passwordGenerator import generate_password
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    password = generate_password()
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    with open("password.txt", mode="a") as pass_file:
        website = website_input.get()
        username = email_input.get()
        password = password_input.get()
        if len(username) == 0 or len(password) == 0 or len(website) == 0:
            var = messagebox.showinfo(title="Oops", message="Empty Fields, Try Again!!!")
        else:
            user_confirmation = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail: {username} "
                                                                              f"\nPassword: {password} \nSave?")
            if user_confirmation:
                password_details = f"{website} | {username} | {password}\n"
                pass_file.write(password_details)
                website_input.delete(0, END)
                password_input.delete(0, END)
                email_input.delete(0, END)
                messagebox.showinfo(title="Success", message="Password Added Successfully!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(width=400, height=400, pady=20, padx=10)
title_label = Label(text="Password Manager", font=("courier", 20, "bold"))
title_label.grid(column=1, row=0)
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)
website_input = Entry(width=35)
website_input.grid(column=1, row=2, columnspan=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=2)
password_input = Entry(width=20)
password_input.grid(column=1, row=4)
generate_button = Button(text="Generate Password", command=get_password)
generate_button.grid(column=2, row=4)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
