
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from pyConnect import *

class newlogin(tk.Tk):

    def __init__(self, parent):

        tk.Tk.__init__(self, parent)
        self.parent = parent
        #self.geometry('300x200')
        self.title('Create a New Account')
        self.init()


    def init(self):
        self.grid()

        self.entry_variable = tk.StringVar()
        self.entry = tk.Entry(self, textvariable = self.entry_variable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.on_Press_Enter)
        self.entry_variable.set(u"Enter Text Here")
        
        button = tk.Button(self,text=u"Click me !", command = self.on_Button_Click)
        button.grid(column=1,row=0)

        self.label_variable = tk.StringVar()
        label = tk.Label(self, textvariable = self.label_variable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.label_variable.set(u"Hello")
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

    def on_Button_Click(self):

        self.label_variable.set(self.entry_variable.get() + " You Clicked!")
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)
        print("You Clicked!")
        
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
