import tkinter

def button_clicked():
    my_label.config(text=input.get())
    print("I got clicked")

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
my_label = tkinter.Label(text=  "I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
# my_label.pack()
my_label.grid(column=0, row=0)

# Buttons
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="new button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
