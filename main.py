from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
import time as t
import math

WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

def start_timer():
    global reps
    reps += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    
    if reps % 8 == 0:
        count_d(long_break_sec)
    elif reps % 2 == 0:
        count_d(short_break_sec)
    else:
        count_d(work_sec)

def count_d(c):
    count_min = math.floor(c/60)
    count_sec = c % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    
    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if c > 0:
        window.after(1000, count_d, c - 1)
    else: 
        start_timer()

window = Tk()
window.title('Pomodoro | Session')

timer_label = Label(text='Session Timer', bootstyle='info', font=('Courier', 25, 'bold'))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=1105, height=500)
img = PhotoImage(file='bgimg.png')
canvas.create_image(550, 250, image=img)

timer = canvas.create_text(555, 250, text='00:00', fill='deepskyblue', font=('Courier', 35, 'bold'))

canvas.tag_lower(canvas.find_all())
canvas.grid(column=1, row=1)

start_btn = Button(text='Start', bootstyle='success-outline', command=start_timer)
reset_btn = Button(text='Reset', bootstyle='danger')

start_btn.grid(column=0, row=1, padx=(250, 0))
reset_btn.grid(column=2, row=1, padx=(0, 250))

window.mainloop()