from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
image = PhotoImage(file='./imgs/Logic-amico (1).png')

height = 600
width = 900
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)


root.config(background="white")


bg_label = Label(root, image=image , bg="white")
bg_label.place(x=290, y=40)

progress_label = Label(root, text="Loading...", font=("Trebuchet Ms", 13, "bold"), fg="#13005A", bg="white")
progress_label.place(x=350, y=500)

progress = ttk.Style()#ttk.Style, qui permet de personnaliser le style des widgets ttk dans une application Tkinter.
progress. theme_use('clam')
progress.configure("red.Horizontal.TProgressbar", background="#13005A")

progress= Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate',
 style="red.Horizontal.TProgressbar")
progress.place(x=250, y=550)

def top():
 root.withdraw()#hide
 os.system("python game.py")#, it's trying to run a Python script named game.py.
 root.destroy()#suppression
 
i=0
def load ():
    global i
    if i<=10:
       txt= 'loading...' + (str(10*i)+'%')
       progress_label.config(text=txt)#Other options that can be modified include fg for text color, bg for background color, font, width, height, state, etc. The exact options available depend on the specific widget.
       progress_label.after(600, load)
       progress['value'] = 10*i
       i +=1
    else:
        top()






load()
root.resizable(False, False)
root.mainloop()
