from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timmer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label_tick.config(text="")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timmer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 2 != 0:
        count_down(work_sec)
        label.config(text="Work")
    elif rep % 2 == 0 and rep != 8:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timmer()
        tick = ""
        for _ in range(math.floor(rep / 2)):
            tick += "✔"
        label_tick.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=350, height=300)
window.config(padx=20, pady=20, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Label

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
label.grid(row=0, column=1)

label_tick = Label(fg=GREEN, bg=YELLOW)
label_tick.grid(row=3, column=1)

# Button

start = Button(text="start", width=5, command=start_timmer)
start.grid(row=2, column=0)

reset = Button(text="reset", width=5, command=reset_timmer)
reset.grid(row=2, column=2)

window.mainloop()
