import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = ""

def right():    
    old_dataset = pandas.read_csv("data/words_to_learn_pt_br_to_en.csv")
    new_dataset = old_dataset[old_dataset.en != current_word]
    with open("data/words_to_learn_pt_br_to_en.csv", mode="w") as file:
        file.write(new_dataset.to_csv(index=False))
    pick_word()

def pick_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_keys)

    while current_word in words_studied:
        current_word = random.choice(words_keys)
    
    words_studied.append(current_word)
    canvas_card.itemconfig(word_text, text=current_word)
    canvas_card.itemconfig(language_text, text="English", fill="black")
    canvas_card.itemconfig(word_text, text=current_word, fill="black")
    canvas_card.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, turn_card)

def turn_card():    
    canvas_card.itemconfig(language_text, text="Brazilian Portuguese", fill="white")
    canvas_card.itemconfig(word_text, text=words_dict[current_word], fill="white")
    canvas_card.itemconfig(card_image, image=card_back_image)


try:
    with open("data/words_to_learn_pt_br_to_en.csv") as file:
        words_dataset = pandas.read_csv("data/words_to_learn_pt_br_to_en.csv")
        print(words_dataset)
except FileNotFoundError:
    words_dataset = pandas.read_csv("data/pt_br_words.csv")
    print(words_dataset.to_csv(index=False))
    with open("data/words_to_learn_pt_br_to_en.csv", mode="w") as file:
        file.write(words_dataset.to_csv(index=False))

words_dict = {row.en:row.pt_br for (index, row) in words_dataset.iterrows()}
words_keys = [key for key in words_dict]

words_studied = []

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, turn_card)

canvas_card = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
card_image = canvas_card.create_image(400, 263, image=card_front_image)
language_text = canvas_card.create_text(400, 150, text="English", fill="black", font=("Ariel", 20, "italic"))
word_text = canvas_card.create_text(400, 263, text="Word", fill="black", font=("Ariel", 50, "bold"))
canvas_card.grid(row=0, column=0, columnspan=2)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, bd=0, pady=0, padx=0, command=pick_word)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, bd=0, pady=0, padx=0, command=right)
right_button.grid(row=1, column=1)

pick_word()

window.mainloop()
