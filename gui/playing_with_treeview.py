from tkinter import *
from tkinter import ttk

r = ["ITEM A", "ITEM B", "ITEM C", "ITEM D", "ITEM E"]
v = ["VALUE A", "VALUE B", "VALUE C", "VALUE D", "VALUE E"]


class App:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("MGT2 Vehicle Designer")


        self.label_frame = ttk.LabelFrame(self.tk, text="Overview", padding="20", )
        self.label_frame.grid(row=0, column=0, sticky='nsew')
        self.frame = ttk.Frame(self.tk, padding='10')
        self.frame.grid(row=0, column=1, sticky='nsew')
        self.label = ttk.Label(self.frame, text='')
        self.label.pack()
        self.tv = ttk.Treeview(self.label_frame, height=3, selectmode='browse', columns=("ITEMS"), show='headings')
        for item in r:
            self.tv.insert("", END, values=item)
        self.tv.heading('ITEMS', text="ITEMS")
        self.scroll = ttk.Scrollbar(self.label_frame, orient=VERTICAL, command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.scroll.set)
        self.tv.bind('<<TreeviewSelect>>', self.on_item_selected)
        self.tv.grid(row=0, column=0, sticky='nsew')
        self.scroll.grid(row=0, column=1, sticky='ns')

        self.tk.mainloop()

    def on_item_selected(self, event):
        self.label.configure(text=str(self.tv.selection()))

def main():
    a = App()


main()
