import tkinter as tk
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
reps = 0
timer = None
work_sessions = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    global work_sessions
    window.after_cancel(timer)
    canvas.itemconfig(timer_countdown,text = "00:00")
    check_marks.config(text = "")
    reps = 0
    work_sessions = 0
    check_marks.config(text=f"Completed: {work_sessions}")

def start_timer():
    global reps
    reps += 1
    work_secs = 5
    shortbreak_secs = 3
    longbreak_secs = 5

    if reps % 8 == 0:
        count_down(longbreak_secs)
        timer_label.config(text = "Long Break", fg = GREEN)
    elif reps % 2 == 0:
        count_down(shortbreak_secs)
        timer_label.config(text="Short Break", fg = GREEN)
    else:
        count_down(work_secs)
        timer_label.config(text=f"Work Mode", fg = PINK)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    mins = math.floor(count/60)
    secs = count % 60
    global timer
    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_countdown, text = f"{mins}:{secs}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else: #start break mode once count reaches to 0
        start_timer()
        global work_sessions
        work_sessions = math.floor(reps / 2)
        check_marks.config(text =f"Completed: {work_sessions}")





# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx= 100, pady = 50 , bg = YELLOW)










timer_label = tk.Label(text = "Pomodoro Timer", font=(FONT_NAME, 22, "bold") )
timer_label.config(padx =5 , pady = 5,fg=RED, bg=YELLOW)

timer_label.grid(row = 0, column = 1)
canvas = tk.Canvas(width = 250, height = 250, bg = YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file = "tomato.png")
canvas.create_image(120, 120, image = tomato_img)
timer_countdown = canvas.create_text(120,140,text = "00:00",fill = "white", font = (FONT_NAME, 35,"bold"))
canvas.grid(row = 1, column = 1)



# start button
start_button = tk.Button(text= "Start" , font=("Arial", 11, "normal"))
start_button.config(bg = PINK, command = start_timer)
start_button.grid(row = 2, column = 0)

# reset button
reset_button = tk.Button(text= "Reset" , font=("Arial", 11, "normal"))
reset_button.config(bg = PINK, command= reset_timer)
reset_button.grid(row = 2, column = 2)





# checkmarks for completed pomodoros
check_marks = tk.Label(text = f"Completed: {work_sessions}", bg = YELLOW, fg = "black" , font = (FONT_NAME, 12, 'bold'))
check_marks.grid(row = 2, column = 1)


window.mainloop()