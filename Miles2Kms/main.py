from tkinter import *


def miles_to_kilo():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609)
    kilometer_output.config(text=f"{kilometers}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=10)

miles_input = Entry(width=10)
miles_input.grid(column=10, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=11, row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=9, row=2)

kilometer_output = Label(text=0)
kilometer_output.grid(column=10, row=2)

kilometer_output_label = Label(text="Kms")
kilometer_output_label.grid(column=11, row=2)

calculate_btn = Button(text="Calculate", command=miles_to_kilo)
calculate_btn.grid(column=10, row=3)

window.mainloop()
