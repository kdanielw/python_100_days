import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    global reps

    reps = 0
    check_label.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps == 4:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)        
    elif reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)        
    else:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    count_sec = int(count % 60)
    count_min = int((count - count_sec) / 60)
    count_timer = f"{count_min:02d}:{count_sec:02d}"
    canvas.itemconfig(timer_text, text=count_timer)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            check_label.config(text="✔️" * int((reps + 1) / 2))
        start_pomodoro()
    

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", command=start_pomodoro)
start_button.grid(row=2, column=0)

start_button = tkinter.Button(text="Reset", command=reset_pomodoro)
start_button.grid(row=2, column=2)

check_label = tkinter.Label(text="", font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

window.mainloop()
