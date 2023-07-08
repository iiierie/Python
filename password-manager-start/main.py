import tkinter as tk
from tkinter import messagebox as mb
import random
import pyperclip
import json
FONT_NAME = "Open Sans"

# ---------------------------- SEARCH ------------------------------- #
def search():
    with open("password.json","r") as password_file:
        website = website_entry.get()
        data = json.load(password_file)

        try:
            username = data[website]["username"]
            password = data[website]["password"]
            pyperclip.copy(password)
            mb.showinfo(title = "Password details", message=f"Email/Username: {username} \n Password: {password}")
        except KeyError:
            mb.showerror(title = "Error", message="Entry not found! ")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def save():
        #get user entered details
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        new_data = {
                    website : {"username" : username,"password" : password}
                    }

        #check simple validation
        if len(password) == 0 or len(username) <= 10 or len(website) == 0:
            if len(username) <= 10:
                mb.showerror(title="Error", message="Please enter your email id or username")
            else:
                mb.showerror(title="Error : Empty Field", message="Don't leave any field empty.")
        else:
            is_ok = mb.askyesno(title=f"{website}", message = f"These are the details entered.\n Email/Username: {username}\n Password: {password} \n All ok to save?")
            if is_ok:
                try:
                    with open ("password.json","r") as password_file:
                        data = json.load(password_file)
                        data.update(new_data)
                except FileNotFoundError:
                    with open("password.json", "w") as password_file:
                        json.dump(new_data, password_file, indent=3)


                else:
                    with open("password.json", "w") as password_file:
                        json.dump(data,password_file, indent= 3)

                finally:
                    website_entry.delete(0, tk.END)
                    username_entry.delete(0, tk.END)
                    password_entry.delete(0, tk.END)
                    username_entry.insert(0,"@gmail.com")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [random.choice(letters) for _ in range(0,random.randint(7,8))]
    password_digits = [random.choice(digits) for _ in range(0,random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(0,random.randint(2,4))]

    password_list = password_symbols+ password_digits+ password_letters
    random.shuffle(password_list)

    password_string = "".join(password_list)
    password_entry.insert(0, password_string)
    pyperclip.copy(password_string)






# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
# window.minsize(width = 300, height = 200)
window.config(padx=15, pady = 15)
window.title("MyPassManager")
canvas = tk.Canvas(height=200, width= 200)
logo = tk.PhotoImage(file= "logo.png")
canvas.create_image(120,120, image = logo)
canvas.grid(row = 0, column = 1)


#all labels
website_label = tk.Label(text="Website:", font=(FONT_NAME, 10, "normal"))
website_label.grid(row = 1 , column = 0, sticky="E")

username_label = tk.Label(text = "Email/Username:")
username_label.grid(row = 2, column = 0)

password_label = tk.Label(text = "Password:")
password_label.grid(row = 3, column = 0, sticky="E")

#all entry fields
website_entry = tk.Entry(width= 26)
website_entry.grid(row = 1 , column = 1,  sticky="E")
website_entry.focus_set()

username_entry = tk.Entry(width = 44)
username_entry.grid(row = 2, column = 1, columnspan=2 , sticky="E")
username_entry.insert(0, "@gmail.com")

password_entry = tk.Entry(width = 26)
password_entry.grid(row = 3, column = 1, sticky="E")



#buttons
search_button = tk.Button(text = "Search", command = search, width=15)
search_button.grid(row = 1 , column = 2, sticky="E")
search_button.config(highlightthickness=0, borderwidth=0)

generate_password_button = tk.Button(text="Generate Password", command = generate_password)
generate_password_button.grid(row = 3, column = 2)
generate_password_button.config(highlightthickness=0, borderwidth=0)

add_button = tk.Button(text  ="Add", width = 37, command=save)
add_button.grid(row = 4, column = 1, columnspan=2, sticky = "E")


# todo: add settings button so that user can choose the length / strength of the password


window.mainloop()
