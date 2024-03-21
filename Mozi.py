from tkinter import * 
from tkinter import messagebox
from ttkbootstrap import *
from ttkbootstrap import Style, Window
from tkinter import ttk
import os
from tkinter import Canvas

def getpath():
    path = os.path.abspath(os.getcwd())
    ujpath = path.replace('\\','/')
    return ujpath
path = getpath()

def fo():
    global tpl1
    tpl1 = Toplevel()
    tpl1.geometry("1400x1200")
    tpl1.title("Mozitown")
    tpl1.iconbitmap("./favicon.ico")
    cim = Label(tpl1, text="Válassz filmet!", font=("Arial", 30))
    cim.pack(pady=10)
    style = Style()
    style.configure("Outline.TMenubutton" , font=("Arial", 20))
    mb = ttk.Menubutton(tpl1, text="Filmek", style='Outline.TMenubutton', direction='below')
    mb.pack()
    menu = Menu(mb, tearoff=False)
    menu.add_command(label="Dűne - Második rész", command=on_menu_select)
    menu.add_command(label="Madame Web", command=lambda: on_menu_select(1))
    menu.add_command(label="Imádlak utálni", command=lambda: on_menu_select(2))
    menu.add_command(label="A méhész", command=lambda: on_menu_select(3))
    menu.add_command(label="Demon Slayer - To the hashira training (Kimetsu No Yaiba)", command=lambda: on_menu_select(4))
    mb.config(menu=menu)
    tpl1.mainloop()

def on_menu_select():
        frame1 = Frame(tpl1)
        frame1.pack(pady=30)
        canvas= Canvas(frame1, width=450, height=665, bg="black")
        canvas.grid(row=0, column=0)
        dunekep = Image.open(path+'/Dűne.png')
        moddune= dunekep.resize((450, 665))
        global keszdune
        keszdune = ImageTk.PhotoImage(moddune)
        canvas.create_image(0, 0, anchor='nw', image=keszdune)
        dunecim = Label(frame1, text="Dűne - Második rész", font=("Arial", 20))
        dunecim.grid(row=0, column=1)7

        


#Főablak
root = Window(themename='vapor')
root.geometry("700x830")
root.title("Mozitown")
root.iconbitmap("./favicon.ico")

kep = Image.open(path+'/MOZITOWN.png')
formazott = kep.resize((500, 750))
megjelen = ImageTk.PhotoImage(formazott)
logo = Label(root, image=megjelen)
logo.pack()

fogomb = Button(root, text="Válassz filmet", style="primary.outline.TButton", bootstyle="primary", command=fo)
fogomb.pack()

mystyle = Style()
mystyle.configure("primary.outline.TButton", font=("Arial", 24))

root.mainloop() 