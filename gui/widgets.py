from tkinter import *
from tkinter import ttk
from .funcs import grid_widget, hide_widget,show_widget

class Designer_Frame:

    def __init__(self, master, /, **kw):
        self.frame_main = ttk.Frame(master, **kw)
        self.children = []

    # this may be the wrong way to go about this one
    def add_child(self, widget, name: str, master, /, **kw):
        """Adds a child Tkinter widget to the parent children list and the parent grid geometry manager"""
        new_child = widget(master, **kw)
        new_child.name = name
        new_child.visible = True
        grid_widget(new_child) # don't know what to do for this yet
        self.children.append(new_child)
        return True

    # not sure if this is the right way to do this
    def remove_child(self, child: str):
        """Removes a child Tkinter widget from the parent children list and the parent grid geometry manager"""
        for _ in self.children:
            if _.name == child:
                _.grid_forget()
                self.children.pop(_)
        return True


class Designer_Label_Frame:

    def __init__(self, master, /, **kw):
        self.frame_main = ttk.LabelFrame(master, **kw)


class Vehicle_Frame(Designer_Label_Frame):

    def __init__(self, master, /, **kw):
        super().__init__(master, **kw)
        self.frame_chas = Chassis_Frame(self.frame_main, text="Chassis")
        self.frame_arms = Armament_Frame(self.frame_main, text="Armaments")


class Chassis_Frame(Designer_Label_Frame):

    def __init__(self, master, /, **kw):
        super().__init__(master, **kw)
        self.frame_cust = Customization_Frame(self.frame_main, text="Customizations")


class Customization_Frame(Designer_Frame):

    def __init__(self, master, /, **kw):
        super().__init__(master, **kw)
        self.entries = []

    def add_button(self, master, item: str, /, **kw) -> bool:
        new_btn = Customization_Button(master, item, **kw)
        # add this to
        self.entries.append(new_btn)
        return True

    def remove_button(self, item: str) -> bool:
        ret = False
        for _ in self.entries:
            if _.item == item:
                self.entries.pop(_)
                ret = True
                break
        return ret


class Armament_Frame(Designer_Label_Frame):

    def __init__(self, master, /, **kw):
        super().__init__(master, **kw)

    def add_mount(self, master, mount: str, row: int, /, **kw):
        """ needs to add a Mount_Frame, and add a new button next to it for the next possible mount"""
        # new_mount = Mount_Frame(master, text=mount, row=row, **kw)
        pass


class Mount_Frame(Designer_Label_Frame):
    def __init__(self, master, /, **kw):
        super().__init__(master, **kw)
        self.weapons = []

    def add_weapon(self, master, weapon: str, /, **kw) -> bool:
        # add a new weapon to self.weapons, draw a new weapon_frame, and draw a new add_button
        pass

    def remove_weapon(self, weapon: str) -> bool:
        pass


class Weapon_Frame(Designer_Frame):

    def __init__(self, master, /, **kw):
        super().__init__(master, **kw)


class Designer_Button:

    def __init_(self, master, /, **kw):
        self.button_main = ttk.Button(master, **kw)


class Customization_Button(Designer_Button):

    def __init__(self, master, item: str, /, **kw):
        self.item = item
        super().__init__(master, text=item, **kw)
