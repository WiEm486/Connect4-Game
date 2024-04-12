#Import the required library
from tkinter import *


import pygame

Acceuil=Tk()
app_width=900
app_height=600
#put the window in the center
screenWidth=Acceuil.winfo_screenwidth()
screenHeight=Acceuil.winfo_screenheight()
x=(screenWidth/2)-(app_width/2)
y=(screenHeight/2)-(app_height/2)
Acceuil.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

Acceuil.title("Connect 4")
Acceuil.resizable(width=FALSE,height=FALSE)
pygame.mixer.init()
pic=PhotoImage(file="./imgs/Sound.png")
def nextPage():
    pygame.mixer.music.stop()
    Acceuil.destroy()
    import main
def play():
   pygame.mixer.music.load("music/alex-productions-extreme-trap-racing-music-power.mp3")
   pygame.mixer.music.play(loops=0)
     
canvas = Canvas(Acceuil,width= 900, height= 600,bg="#13005A",border=0,highlightbackground="#13005A")
img=PhotoImage(file="./pngtree-abstract-80s-trendy-geometric-background-neon-colors-picture-image_1157555.png")

canvas.create_image(0,0,anchor=NW,image=img)





canvas.place(x=0,y=0)
canva = Canvas(Acceuil,width= 1000, height= 200,bg="#13005A",bd=0,highlightbackground="#13005A")

img1=PhotoImage(file="./Capture d’écran 2023-01-14 130600-removebg-preview.png")
canva.create_image(10,0,anchor=NW,image=img1)
canva.place(x=-15,y=0)
picture=PhotoImage(file="./imgs/play (1).png")
mybutton=Button(Acceuil,image=picture,command=nextPage)
mybutton.place(x=350,y=320)
my_button=Button(Acceuil,image=pic,command=play,bg="#13005A",bd=0)
my_button.place(x=810,y=480)

Acceuil.mainloop()