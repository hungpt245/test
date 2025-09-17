import pyttsx3
import ctypes
import googletrans
from googletrans import Translator
from tkinter import *
from PIL import Image, ImageTk

engine = pyttsx3.init()
root = Tk()
root.title('C to F converter')
root.geometry("500x630")
root.iconbitmap('logo.ico')

load = Image.open('background.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text="Converter, Translater",fg="#FFFFFF",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",20))
name.pack(pady=10)

box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def convert():
    box1.delete(1.0,END)
    cTem = box.get(1.0,END)
    # print(type(cTem))
    while cTem:
        if cTem=="":
            ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
            continue
        else:
            cTem = float(cTem)
            fTem = round(9/5 * cTem + 32,1)
            box1.insert(END,fTem)               
            break
def translate():
    box1.delete(1.0,END)
    INPUT = box.get(1.0,END)
    t=Translator()
    a=t.translate(INPUT,src="vi",dest="en")
    b=a.text
    box1.insert(END,b)
    engine.say(b)
    engine.runAndWait()
    
def translate1():
    box1.delete(1.0,END)
    INPUT = box.get(1.0,END)
    t=Translator()
    a=t.translate(INPUT,src="en",dest="vi")
    b=a.text
    box1.insert(END,b)

clear_button=Button(button_frame,text="Clear text",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=clear)
clear_button.place(x=50,y=310)
convert_button=Button(button_frame,text="Convert",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=convert)
convert_button.place(x=170,y=310)
transerlate_button=Button(button_frame,text="VI to EN",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate)
transerlate_button.place(x=250,y=310)
transerlate_button1=Button(button_frame,text="EN to VI",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate1)
transerlate_button1.place(x=360,y=310)

box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)

root.mainloop()
