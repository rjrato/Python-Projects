from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from cryptography.fernet import Fernet
import pyperclip
import json

FONT_NAME = "Courier"
BUTTON = "#9DB2BF"
BUTTON_CLICK = "#526D82"
BUTTON_ON_HOVER = "#DDE6ED"
CHARACTERS = "#fefff8"
DARK_BLUE = "#001c32"
SAVE_BUTTON = "#BFD8AF"
SAVE_BUTTON_CLICK = "#99BC85"
SAVE_BUTTON_ON_HOVER = "#E1F0DA"


# ---------------------------- GENERATE KEY ------------------------------- #
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


# generate_key()


# ---------------------------- LOAD KEY ------------------------------- #
def load_key():
    return open("secret.key", "rb").read()


key = load_key()
f = Fernet(key)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = random_letters + random_symbols + random_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)


# ---------------------------- GET PASSWORD ------------------------------- #
def search_password():
    website_provided = website_entry.get().capitalize()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found!")
        return
    except json.JSONDecodeError:
        messagebox.showwarning(title="Error", message="Error reading the data file!")
        return
    else:
        if len(website_provided) == 0:
            messagebox.showwarning(title="Oops", message="Please enter the Website to search your Password.")
        elif website_provided not in data:
            messagebox.showwarning(title="Error", message="Website not found.")
        else:
            encrypted_password = data[website_provided]["password"]
            password = f.decrypt(encrypted_password.encode()).decode()
            messagebox.showinfo(title=f"{website_provided} Password", message=f"{website_provided} account found. Your password was copied to clipboard, please proceed to {website_provided} website and past it.")
            pyperclip.copy(password)

    finally:
        website_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 and len(password) == 0:
        messagebox.showwarning(title="Oops", message=f"Please enter the Website and Password.")
        website_entry.focus()
    elif len(website) == 0:
        messagebox.showwarning(title="Oops", message=f"Please enter the Website.")
        website_entry.focus()
    elif len(password) == 0:
        messagebox.showwarning(title="Oops", message=f"Please enter the Password.")
        password_entry.focus()
    else:
        try:
            encrypted_password = f.encrypt(password.encode()).decode()

            entry = {
                website: {
                    "email": email,
                    "password": encrypted_password,
                }
            }

            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            if messagebox.askokcancel(title=website,
                                      message=f"Account: {website}\nUsername: {email}\nPassword: {password}\nDo you confirm this information?"):
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

                pyperclip.copy(password)
                messagebox.showinfo(title="Ready to go!", message="Successfully saved!\nYour new password was copied to clipboard!")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            else:
                pass
        else:
            if website in data:
                if messagebox.askokcancel(title="Account found", message=f"Account already saved.\nYour current password is {data[website]["password"]}\nWant update your password?"):
                    with open("data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)
                        # Updating old data with new data
                        data.update(entry)
                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)

                    pyperclip.copy(password)
                    messagebox.showinfo(title="Ready to go!", message="Successfully saved!\nYour new password was copied to clipboard!")

                else:
                    pass

                website_entry.delete(0, END)
                password_entry.delete(0, END)

            else:
                if messagebox.askokcancel(title=website, message=f"Account: {website}\nUsername: {email}\nPassword: {password}\nDo you confirm this information?"):
                    with open("data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)
                        # Updating old data with new data
                        data.update(entry)

                    pyperclip.copy(password)
                    messagebox.showinfo(title="Ready to go!", message="Successfully saved!\nYour new password was copied to clipboard!")

                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)
                else:
                    pass

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("ShieldPass Vault")
window.config(padx=20, pady=20, bg=DARK_BLUE)
window.columnconfigure(0, minsize=125, weight=0)
window.columnconfigure(1, minsize=125, weight=0)
window.columnconfigure(2, minsize=125, weight=0)

title = Label(text="ShieldPass Vault", fg=CHARACTERS, bg=DARK_BLUE, font=(FONT_NAME, 16, "bold"))
title.grid(column=1, row=0)

logo_img = PhotoImage(file="logo.png")
logo = Canvas(width=280, height=300, bg="#526D82", highlightthickness=0)
logo.create_image(135, 150, image=logo_img)
logo.grid(column=1, row=1)

website_label = Label(text="Account", fg=CHARACTERS, bg=DARK_BLUE, font=(FONT_NAME, 12, "bold"), pady=10, padx=10)
website_entry = Entry(width=27, borderwidth=2)
website_entry.focus()
email_label = Label(text="Email", fg=CHARACTERS, bg=DARK_BLUE, font=(FONT_NAME, 12, "bold"), pady=10, padx=10)
email_entry = Entry(width=50, borderwidth=2)
password_label = Label(text="Password", fg=CHARACTERS, bg=DARK_BLUE, font=(FONT_NAME, 12, "bold"), pady=10, padx=10)
password_entry = Entry(width=27, borderwidth=2)
password_gen = Button(width=10, text="Generate", fg=DARK_BLUE, bg=BUTTON, activebackground=BUTTON_CLICK, font=(FONT_NAME, 12, "bold"), command=pass_generator)
save_btn = Button(window, width=10, text="Save", fg=DARK_BLUE, bg=SAVE_BUTTON, activebackground=SAVE_BUTTON_CLICK, font=(FONT_NAME, 12, "bold"), command=save_entry)
search_password_btn = Button(window, width=10, text="Search", fg=DARK_BLUE, bg=BUTTON, activebackground=BUTTON_CLICK, font=(FONT_NAME, 12, "bold"), command=search_password)
signature = Label(text="built and designed by Ricardo Rato", fg=CHARACTERS, bg=DARK_BLUE, font=(FONT_NAME, 8, "normal"), pady=10, padx=10)

website_label.grid(column=0, row=2, sticky="e")
website_entry.grid(column=1, row=2, sticky="w")
email_label.grid(column=0, row=3, sticky="e")
email_entry.grid(column=1, row=3, sticky="w")
email_entry.insert(0, "ricardo.jorge.rato@gmail.com")
password_label.grid(column=0, row=4, sticky="e")
password_entry.grid(column=1, row=4, sticky="w")
password_gen.grid(column=1, row=4, sticky="e")
search_password_btn.grid(column=1, row=2, pady=10, sticky="e")
save_btn.grid(column=1, row=5, pady=10, sticky="e")
signature.grid(column=1, row=6)


# ---------------------------- BUTTON HOVERING------------------------------- #
def password_gen_on_enter(e):
    password_gen.config(background=BUTTON_ON_HOVER, foreground=DARK_BLUE)


def password_gen_on_leave(e):
    password_gen.config(background=BUTTON, foreground=DARK_BLUE)


def search_password_btn_on_enter(e):
    search_password_btn.config(background=BUTTON_ON_HOVER, foreground=DARK_BLUE)


def search_password_btn_on_leave(e):
    search_password_btn.config(background=BUTTON, foreground=DARK_BLUE)


def save_btn_on_enter(e):
    save_btn.config(background=SAVE_BUTTON_ON_HOVER, foreground=DARK_BLUE)


def save_btn_on_leave(e):
    save_btn.config(background=SAVE_BUTTON, foreground=DARK_BLUE)


password_gen.bind("<Enter>", password_gen_on_enter)
password_gen.bind("<Leave>", password_gen_on_leave)
search_password_btn.bind("<Enter>", search_password_btn_on_enter)
search_password_btn.bind("<Leave>", search_password_btn_on_leave)
save_btn.bind("<Enter>", save_btn_on_enter)
save_btn.bind("<Leave>", save_btn_on_leave)

window.mainloop()
