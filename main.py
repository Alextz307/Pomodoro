from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECOND_TO_MS = 1000
MINUTE_TO_SECONDS = 60

reps = 0
timer = 'None'


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    checkmark_label.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * MINUTE_TO_SECONDS
    short_break_seconds = SHORT_BREAK_MIN * MINUTE_TO_SECONDS
    long_break_seconds = LONG_BREAK_MIN * MINUTE_TO_SECONDS

    if reps % 2 == 1:
        req_seconds = work_seconds
        title_label.config(text='Work', fg=GREEN)
    elif reps % 8 == 0:
        req_seconds = long_break_seconds
        title_label.config(text='Break', fg=RED)
    else:
        req_seconds = short_break_seconds
        title_label.config(text='Break', fg=PINK)

    count_down(req_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def convert_to_minutes(seconds):
    minutes = seconds // MINUTE_TO_SECONDS
    remaining_seconds = seconds % MINUTE_TO_SECONDS
    return f'{minutes:02}:{remaining_seconds:02}'


def count_down(count):
    canvas.itemconfig(timer_text, text=convert_to_minutes(count))
    if count > 0:
        global timer
        timer = window.after(SECOND_TO_MS, count_down, count - 1)
    else:
        start_timer()
        checkmarks = '✔' * (reps // 2)
        checkmark_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Time Tracking')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(row=0, column=1)


def create_button(new_text, new_row, new_column, is_start):
    new_button = Button(text=new_text, bg='white', highlightbackground=YELLOW)
    new_button.grid(row=new_row, column=new_column)

    if is_start:
        new_button.config(command=start_timer)
    else:
        new_button.config(command=reset_timer)

    return new_button


start_button = create_button('Start', 2, 0, True)
reset_button = create_button('Reset', 2, 2, False)

checkmark_label = Label()
checkmark_label.config(bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()
