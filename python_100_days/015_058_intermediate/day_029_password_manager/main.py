import tkinter
import tkinter.messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        message_empty = f"Please don't leave any fields empty"
        tkinter.messagebox.showwarning(title=website, message=message_empty)
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:        
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

# --------------------------- SEARCH SITE ------------------------------ #
def search_site():
    website = website_entry.get()
    if len(website) == 0:
        tkinter.messagebox.showwarning(title=website, message="Please type the website")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)                
        except:
            tkinter.messagebox.showerror(title="Error", message="You don't have any account saved.")
        else:
            if website in data:
                data_website = data[website]
                tkinter.messagebox.showinfo(title=website, message=f"Username: {data_website["username"]}\nPassword: {data_website["password"]}")
            else:
                tkinter.messagebox.showerror(title="Website Not Found", message=f"The website {website} was not found.")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tkinter.Button(text="Search", command=search_site, width=10)
search_button.grid(row=1, column=2)

username_label = tkinter.Label(text="Email / Username:")
username_label.grid(row=2, column=0)

username_entry = tkinter.Entry(width=43)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "dnaniel@email.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=30)
password_entry.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generate", command=generate_password, width=10)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", command=add_password, width=41)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
