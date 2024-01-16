from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title('Pomodoro | Session')
timer_label = Label(text='Session Timer',bootstyle='info', font=('Courier', 25, 'bold'))
timer_label.grid(column=1, row=0)
canvas = Canvas(width=1105, height=500)
img = PhotoImage(file='bgimg.png')
canvas.create_image(550,250, image=img)
canvas.create_text(555,250, text='00:00', fill='deepskyblue', font=('Courier', 35, 'bold'))
canvas.tag_lower(canvas.find_all())
canvas.grid(column=1, row=1)
start_btn = Button(text='Start', bootstyle='success-outline')
reset_btn = Button(text='Reset', bootstyle='danger')
start_btn.grid(column=0, row=1, padx=(250,0))
reset_btn.grid(column=2, row=1, padx=(0,250))

window.mainloop()
