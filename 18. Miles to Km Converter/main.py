# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

import tkinter

window = tkinter.Tk()
window.title("Mile to km Converter")
window.minsize(width=400,height=200)
window.config(padx=50,pady=50)

FONT = ("Arial",15)

# create a function that will convert the user input to an int and then convert it from miles to km
def calculate():
    try:
        number =float(user_input.get())
        result = round(number * 1.609,2)
        # an important step here is that i need to convert the result into a string
        # there are several ways i could do this
        # one is result_label.config(text=f"{result}")
        # another is below
        result_label.config(text=str(result))

    except ValueError:
        result_label.config(text=str(f"Invalid, please enter an integer."))

# create "is equal to label"
my_label = tkinter.Label(text="is equal to",font=FONT)
my_label.grid(column=0,row=1)

# create Miles label
my_label_2 = tkinter.Label(text="Miles",font=FONT)
my_label_2.grid(column=2,row=0)

# create km label
my_label_3 = tkinter.Label(text="Km", font=FONT)
my_label_3.grid(column=2,row=1)

# In addition to labels, we can also create buttons
# (as a side note if we start the page with from tkinter import *, we can remove all of the "tkinter" mentions)

# create entry widget
user_input = tkinter.Entry(width=10)
user_input.grid(column=1,row=0)

# create result label
result_label = tkinter.Label()
result_label.grid(column=1,row=1)

# create button label
button = tkinter.Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)


window.mainloop()
