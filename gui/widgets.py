from tkinter import *
from tkinter import ttk



class Label_Frame:

    def __init__(self, master, /, **kw):
        self.frame_main = ttk.LabelFrame(master, **kw)





class Vehicle_Frame(Label_Frame):

    def __init__(self, master, /, **kw):
        super().__init__(master, **kw)



