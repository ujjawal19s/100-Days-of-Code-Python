from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])

    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password_name,
        }
    }

    if len(website_name) == 0 or len(password_name) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with the new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    web = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if web in data:
            email_name = data[web]["email"]
            password_name = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email_name}\nPassword: {password_name}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")

canvas.create_image(100, 95, image=pass_img)
canvas.grid(row=0, column=1)

# Lable

website = Label(text="Website:", font=("Arial", 12, "normal"))
website.grid(row=1, column=0)

email = Label(text="Email/Username:", font=("Arial", 12, "normal"))
email.grid(row=2, column=0)

password_ui = Label(text="Password:", font=("Arial", 12, "normal"))
password_ui.grid(row=3, column=0)

# entry

website_entry = Entry(width=45)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ujjawal23@gmail.com")

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

# Button

pass_button = Button(width=15, height=1, text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2)

add_button = Button(width=38, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(width=10, text="Search", command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
