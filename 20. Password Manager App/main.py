# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #create a conditional statement so that the function will only run if the
    # password entry box is empty
    if len(password_entry.get()) == 0:
        # generate sets of random letters, symbols, and numbers
        password_letters = [random.choice(letters) for _ in range(random.randint(6,8))]
        password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
        password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
        # combine these sets together and shuffle
        password = password_letters + password_symbols + password_numbers
        random.shuffle(password)
        # combine with join to remove from lists, insert into the password_entry box and make a copy onto the clipboard
        final_password = "".join(password)
        password_entry.insert(0,f"{final_password}")
        pyperclip.copy(final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # website name
    website_to_save = website_entry.get()
    # password
    password_to_save = password_entry.get()
    # email used
    email_to_save = email_entry.get()

    # if website, password, or email boxes are empty, produce an error message informing user to fill them out
    if len(website_to_save) == 0 or len(password_to_save) == 0 or len(email_to_save) == 0:
        messagebox.showinfo(title="Error",message="Please do not leave any fields empty.")
    else:
        # create a message box confirming with the user the details of the information before save is initiated
        is_ok = messagebox.askokcancel(title=website_to_save,message=f"These are the details entered: \nEmail: {email_to_save} "
                                                         f"\nPassword: {password_to_save} \nIs it ok to save?")
        if is_ok:
            # create new .txt file and save the three pieces of information in their own row
            with open("Password_Storage.txt", "a") as write_password:
                write_password.write(f"{website_to_save},{email_to_save},{password_to_save} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Storage")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
canvas.grid(column=1,row=0)

image = PhotoImage(file="logo.png")

canvas.create_image(100,100,anchor="center", image=image)

# website label
website_label = Label(text="Website")
website_label.grid(column=0,row=1)

# website entry field
website_entry = Entry(bg="white",width=38)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

#email/username label
email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)

# email entry field
email_entry = Entry(bg="white",width=38)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"tjsmelter@gmail.com")

#password label
password_label = Label(text="Password")
password_label.grid(column=0,row=3)

# password entry field
password_entry = Entry(bg="white",width=21)
password_entry.grid(column=1,row=3)

# generate password button
password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(column=2,row=3)

# add button 
add_button = Button(text="Add",width=36, command=save_password)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()
