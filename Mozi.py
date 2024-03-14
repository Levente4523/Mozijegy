from tkinter import * 
from tkinter import messagebox
from ttkbootstrap import *

def fo():
    tpl1 = Toplevel()
    tpl1.geometry("1000x800")
    tpl1.title("Mozitown")
    tpl1.iconbitmap("./favicon.ico")
    cim = Label(tpl1, text="Válassz filmet!", font=("Arial", 30))
    cim.pack(pady=10)
    tpl1.mainloop()


#Főablak
root = Window(themename='vapor')
root.geometry("700x830")
root.title("Mozitown")
root.iconbitmap("./favicon.ico")

kep = Image.open('J:\IKT (python)\Mozijegy\MOZITOWN.png')
formazott = kep.resize((500, 750))
megjelen = ImageTk.PhotoImage(formazott)
logo = Label(root, image=megjelen)
logo.pack()

fogomb = Button(root, text="Válassz filmet", style="primary.outline.TButton", bootstyle="primary", command=fo)
fogomb.pack()

mystyle = Style()
mystyle.configure("primary.outline.TButton", font=("Arial", 24))

root.mainloop() 