from tkinter import *
from PIL import ImageTk, Image
import os, sys
from pyautogui import alert
from random import sample
from particulasConPausaGravedad import run


class GUI(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        frame_base = Frame(self)
        frame_base.pack()
        self.frames = {}
        #el equivalente a hacer una variable global en este metodo es hacer
        #a las variables que quieras usar en otros frames, parte de la clase ppal,
        #cosa de poder acceder a esas variables mediante controller.variablex

        frame = Pagina_ppal(frame_base, self)
        self.frames[Pagina_ppal] = frame
        frame.grid(row=0, column=0, sticky="nsew")

            
        self.mostrar_frame(Pagina_ppal)
    def mostrar_frame(self, frame):
        frame = self.frames[frame]
        frame.tkraise()

class Pagina_ppal(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(width=500, height=600)
        pathFile = os.path.dirname(os.path.realpath(sys.argv[0]))
        imgName = r"explicacionChoque.png"
        pathImg = pathFile+ r"\\" + imgName
        self.img = ImageTk.PhotoImage(Image.open(pathImg))
        self.label_img = Label(self, image=self.img)
        self.label_img.place(relx=0.5, rely=0.5, anchor=CENTER)
        #creo un label para la masa de la particula 1
        self.label_1 = Label(self, text="Masa particula 1")
        self.label_1.place(x=10, y=450, anchor=W)
        #creo una entry
        self.e_1 = Entry(self)
        self.e_1.place(x=170, y=450, anchor=W)
        #creo un label para el tamaño de la particula 1
        self.label_2 = Label(self, text="Tamaño particula 1")
        self.label_2.place(x=10, y=475, anchor=W)
        #creo una entry
        self.e_2 = Entry(self)
        self.e_2.place(x=170, y=475, anchor=W)
        #creo un label para la masa de la particula 2
        self.label_3 = Label(self, text="Masa particula 2")
        self.label_3.place(x=10, y=500, anchor=W)
        #creo una entry
        self.e_3 = Entry(self)
        self.e_3.place(x=170, y=500, anchor=W)
        #creo un label para el tamaño de la particula 2
        self.label_4 = Label(self, text="Tamaño particula 2")
        self.label_4.place(x=10, y=525, anchor=W)
        #creo una entry
        self.e_4 = Entry(self)
        self.e_4.place(x=170, y=525, anchor=W)
        self.boton_1 = Button(self, text="Jugar",
                              command=lambda:correr(self))
        self.boton_1.place(relx=0.5, rely=0.5, anchor=CENTER)

            
        def correr(self):
            if self.e_1.get() == "":
                masa1 = 30
            else:
                masa1 = int(self.e_1.get())
            if self.e_2.get() == "":
                size1 = 30
            else:
                size1 = int(self.e_2.get())
            if self.e_3.get() == "":
                masa2 = 80
            else:
                masa2 = int(self.e_3.get())
            if self.e_4.get() == "":
                size2 = 30
            else:
                size2 = int(self.e_4.get())
            run(masa1, masa2, size1, size2)

        
            
   

"""
Al trabajar con clases de este modo, cada vez que crees un objeto de la clase
botones, dicho objeto se va a pasar como self por default y va a hacer lo que
sea que este en el init method, no es necesario llamar a ninguna funcion, ya
que desde el init method se estan llamando a otras funciones.

"""







