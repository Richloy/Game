
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from pyConnect import *

class newlogin(tk.Tk):

    def __init__(self, parent):

        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry('300x200')
        self.title('Create a New Account')
        notebook = ttk.Notebook(self)
        self.frame1 = ttk.Frame(notebook)
        self.frame2 = ttk.Frame(notebook)
        self.frame3 = ttk.Frame(notebook)
        self.frame4 = ttk.Frame(notebook)
        notebook.add(self.frame1, text='Name')
        notebook.add(self.frame2, text='Gender')
        notebook.add(self.frame3, text='Clothes')
        notebook.add(self.frame4, text='Hair')
        notebook.pack()
        self.init()


    def init(self):

        self.entry_variable = tk.StringVar()
        self.entry = tk.Entry(self.frame1, textvariable = self.entry_variable)
        self.entry.bind("<Return>", self.on_Press_Enter)
        self.entry.pack(anchor=tk.W)

        self.password_variable = tk.StringVar()
        self.password = tk.Entry(self.frame1, textvariable = self.password_variable)
        self.password.bind("<Return>", self.on_Press_Enter)
        self.password.pack()
        
        self.button = tk.Button(self.frame1,text=u"Click me !", command = self.on_Button_Click)
        self.button.pack()

        self.label_variable = tk.StringVar()
        self.label = tk.Label(self.frame1, textvariable = self.label_variable,
                              anchor="w",fg="white",bg="blue")
        self.label_variable.set(u"Hello")
        self.label.pack()
        
        #self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

    def on_Button_Click(self):

        self.label_variable.set(self.entry_variable.get() + " You Clicked!")
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)
        print("You Clicked!")
        print(self.entry_variable.get())
        
    def on_Press_Enter(self, event):

        self.label_variable.set(self.entry_variable.get() + " You Pressed Enter!")
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)
        print("You Pressed Enter!")
        
    def running(self):
        print("new login started")


if __name__ == "__main__":
    app = newlogin(None)
    app.mainloop()
