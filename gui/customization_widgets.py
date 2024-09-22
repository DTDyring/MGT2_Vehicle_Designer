from tkinter import *
from tkinter import ttk


class Customization_Frame:
    """Generic container for Customization selection GUI elements"""

    # using "**kw" because that's how ttk is signed, and I don't know if that would conflict with my usual approach
    def __init__(self, master, **kw):
        # master should be the parent that owns the Customization_Frame
        self.frame_main = ttk.Frame(master, **kw)
        self.c_btns = []

    def add_btn(self, item: str):
        # doesn't do everything it's supposed to do yet
        new_btn = Customization_Button(self, text=item)
        self.c_btns.append(new_btn)
        return True


# may not need this?
class Customization_Button:
    """Button for customizations"""

    def __init__(self, master, /, **kw):
        self.btn = ttk.Button(master, **kw)



