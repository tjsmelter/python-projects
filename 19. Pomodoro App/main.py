# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from tkinter import *
import math
import pygame

pygame.mixer.init()

def play_tone():
    pygame.mixer.music.load("/Users/ThomasSmelter/Desktop/Python/Sounds/ui-sound-on-270295.mp3")
    pygame.mixer.music.play()
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
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    top_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_b_sec = SHORT_BREAK_MIN * 60
    long_b_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        update_timer(long_b_sec)
        top_label.config(text="Long Break",font=(FONT_NAME,35,"normal"),bg=YELLOW,fg=RED,highlightthickness=0)
    elif reps % 2 == 0:
        update_timer(short_b_sec)
        top_label.config(text="Short Break", font=(FONT_NAME, 35, "normal"), bg=YELLOW, fg=PINK, highlightthickness=0)
    else:
        update_timer(work_sec)
        top_label.config(text="Work", font=(FONT_NAME, 35, "normal"), bg=YELLOW, fg=GREEN, highlightthickness=0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def update_timer(time):
    minutes = math.floor(time / 60)
    seconds = time % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")

    if time > 0:
        global timer
        timer = window.after(1000,update_timer, time-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(math.floor(work_sessions)):
            marks += "✔"
        check_mark.config(text=marks)
        play_tone()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

# create canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.grid(column=1,row=1)

# add image
image = PhotoImage(file="tomato.png")

# add timer text
canvas.create_image(100,112,anchor="center",image=image)
timer_text = canvas.create_text(100, 130,text="0:00",fill="white",font=(FONT_NAME,30,"bold"))

# add text at the top
top_label = Label(text="Timer",font=(FONT_NAME,35,"normal"),bg=YELLOW,fg=GREEN,highlightthickness=0)
top_label.grid(column=1,row=0)

# add check marks
check_mark = Label(fg=GREEN,bg=YELLOW,highlightthickness=0)
check_mark.grid(column=1,row=3)

# add start button
start_button = Button(text="Start",command=start_timer,highlightthickness=0)
start_button.grid(column=0,row=2)

# add reset button
reset_button = Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_button.grid(column=2,row=2)

window.mainloop()
