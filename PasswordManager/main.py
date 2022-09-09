from tkinter import *
from tkinter import messagebox
from passwordGenerator import generate_password
import pyperclip
import json


def search_password():
    try:
        with open("data.json", "r") as search_data:
            website = website_input.get().lower()
            data = json.load(search_data)

    except FileNotFoundError:
        print("No data file found")
        messagebox.showinfo(title="Error", message="No data file found.")
    else:

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            var = messagebox.showinfo(title="Success", message=f"The Account details for {website.title()} are:\nEmail: {email}\nPassword: {password} ")
        else:
            var = messagebox.showinfo(title="Oops", message=f"No account found for {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    password = ""
    password = generate_password()
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        var = messagebox.showinfo(title="Oops", message="Empty Fields, Try Again!!!")
    else:
        user_confirmation = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail: {email} "
                                                                          f"\nPassword: {password} \nSave?")
        if user_confirmation:
            try:
                with open("data.json", "r") as pass_file:
                    data = json.load(pass_file)

            except FileNotFoundError:
                with open("data.json", "w") as pass_file:
                    json.dump(new_data, pass_file, indent=4)

            else:
                with open("data.json", "w") as pass_file:
                    data.update(new_data)
                    json.dump(data, pass_file, indent=4)

            finally:
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
website_input = Entry(width=36)
website_input.grid(column=1, row=2, sticky=W, padx=30, columnspan=2)
email_input = Entry(width=36)
email_input.grid(column=1, row=3, sticky=W, padx=30, columnspan=2)
password_input = Entry(width=36)
password_input.grid(column=1, row=4, sticky=W, padx=30)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=2, sticky=W)

generate_button = Button(text="Generate Password", width=15, command=get_password)
generate_button.grid(column=2, row=4, sticky=W)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
