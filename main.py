from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title('Pomodoro | Session')

canvas = Canvas(width=1500, height=500)
img = PhotoImage(file='bgimg.png')
canvas.create_image(-395,750, image=img)
canvas.create_text(590,250, text='00:00', fill='blue', font=('Courier', 35, 'bold'))
canvas.pack()
window.mainloop()