from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Error", message="Invalid entry. Missing one or more values.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered:\nEmail/Username: {username}\n"
                                                              f"Password: {password}\nSave this data?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=1)

password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=3, column=2, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.grid(row=4, column=2, sticky="W")

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=4, column=3, sticky="EW")

add = Button(text="Add", width=36, command="save")
add.grid(row=5, column=2, columnspan=2, sticky="EW")

window.mainloop()