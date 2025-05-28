from tkinter import *
import requests
import random


def get_quote():
    response = requests.get(url="https://zenquotes.io/api/quotes/")
    response.raise_for_status()
    data = response.json()
    selected_response = random.choice(data)
    print(selected_response)

    quote = selected_response["q"]
    author = selected_response["a"]

    canvas.itemconfig(quote_text, text=quote)
    author_label.config(text=author)
    window.title(f"{author} Says")


window = Tk()
window.title("Someone Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Someone Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

author_label = Label(text="Author", font=("Arial", 20, "bold"))
author_label.grid(row=1, column=0)

author_button = Button(text="Next Quote", highlightthickness=0, command=get_quote)
author_button.grid(row=2, column=0)

get_quote()

window.mainloop()
