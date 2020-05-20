#import os
from tkinter import *
from tkinter.ttk import Combobox
import playsound
from gtts import gTTS

fen = Tk()
fen.title("Text to speech application")
fen.iconbitmap("marrakech_yds_icon.ico")
fen.minsize(720,300)
fen.config(background='#5f6af2')

image = PhotoImage(file="voice.png").zoom(24).subsample(64)

def speak():
    language = listb.get()
    mytext = ent.get()
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("output1.mp3")
    playsound.playsound('output1.mp3', True)

frm = Frame(fen,bg='#5f6af2')

can = Canvas(frm,height=200,width=200,bg='#5f6af2',bd=0,highlightthickness=0)
can.create_image(100,100,image=image)
can.pack()

lab = Label(frm,text="Ecrivez une phrase",font=('Verdana',12),fg='white',bg='#5f6af2')
lab.pack()

ent = Entry(frm,font=('Verdana',18),fg='white',bg='#5f6af2')
ent.pack()

listb = Combobox(frm, values=['en',
                              'ar'],font=('Verdana',12))
listb.insert(END, 'en')
listb.insert(END, 'ar')
listb.current(0)
listb.pack(expand=YES)

but = Button(frm, bg='#7079e7', font=('Verdana',12), fg='white', text="Entendre", bd=0, command=speak)
but.pack()

frm.pack()

fen.mainloop()