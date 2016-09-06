''' Login Using Frames'''

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
        #root = Tk()

        self.label_variable = tk.StringVar()
        self.label = tk.Label(self, textvariable = self.label_variable,
                              anchor="w",fg="white",bg="blue")
        self.label_variable.set(u"Hello")
        self.label.pack()
        
        self.login_frame = ttk.Labelframe(self, text = 'Credentials', borderwidth = 5)
        self.gender_frame = ttk.Labelframe(self, text = 'Select Gender')
        
        '''self.frame1 = ttk.Frame(notebook)
        self.frame2 = ttk.Frame(notebook)
        self.frame3 = ttk.Frame(notebook)
        self.frame4 = ttk.Frame(notebook)
        notebook.add(self.frame1, text='Name')
        notebook.add(self.frame2, text='Gender')
        notebook.add(self.frame3, text='Clothes')
        notebook.add(self.frame4, text='Hair')
        notebook.pack()'''
        self.user_credentials()


    def user_credentials(self):
        self.login_frame.pack()
        self.grid()
        
        self.user_label = tk.Label(self.login_frame, text="Username", fg="red")
        #redbutton.pack(anchor = tk.NW)
        self.user_label.grid(column=0, row=0)

        self.user_entry_variable = tk.StringVar()
        self.user_entry = tk.Entry(self.login_frame, textvariable = self.user_entry_variable, fg="brown")
        #brownbutton.pack(anchor = tk.NW)
        self.user_entry.grid(column=1, row=0)

        seperator = tk.Label(self.login_frame, text="")
        #redbutton.pack(anchor = tk.NW)
        seperator.grid(column=0, row=1, sticky='EW')
        
        self.user_pwd_label = tk.Label(self.login_frame, text="Password", fg="red")
        #redbutton.pack(anchor = tk.NW)
        self.user_pwd_label.grid(column=0, row=2, sticky='EW')

        self.user_pwd_variable = tk.StringVar()
        self.user_pwd_entry = tk.Entry(self.login_frame, textvariable = self.user_pwd_variable, fg="brown")
        #brownbutton.pack(anchor = tk.NW)
        self.user_pwd_entry.grid(column=1, row=2)

        '''self.entry_variable = tk.StringVar()
        self.entry = tk.Entry(self.frame1, textvariable = self.entry_variable)
        self.entry.bind("<Return>", self.on_Press_Enter)
        self.entry.pack(anchor=tk.W)

        self.password_variable = tk.StringVar()
        self.password = tk.Entry(self.frame1, textvariable = self.password_variable)
        self.password.bind("<Return>", self.on_Press_Enter)
        self.password.pack()'''
        
        self.button = tk.Button(self.login_frame,text=u"Gender ->", command = self.on_Button_Click)
        self.button.grid(column=1,row=3)
        
        #self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.user_entry.focus_set()
        self.user_entry.selection_range(0, tk.END)

    def user_gender(self):
        print("Select Gender")

        self.gender_frame.pack()
        self.grid()
        v = tk.IntVar()
        
        self.gender_radio1 = tk.Radiobutton(self.gender_frame, text = "Male", variable = v, value = 0, indicatoron = 1)
        self.gender_radio1.grid(column=0, row=0, sticky = 'W')

        self.gender_radio2 = tk.Radiobutton(self.gender_frame, text = "Female", variable = v, value = 1, indicatoron = 1)
        self.gender_radio2.grid(column=0, row=1, sticky = 'W')
        self.update()

    def on_Button_Click(self):

        self.label_variable.set("Welcome " + self.user_entry_variable.get())
        self.user_entry.focus_set()
        self.user_entry.selection_range(0, tk.END)
        print("You Clicked!")
        print(self.user_entry_variable.get())
        print(self.user_pwd_variable.get())
        self.login_frame.destroy()
        self.user_gender()
        
    def on_Press_Enter(self, event):

        self.label_variable.set("Welcome " + self.entry_variable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)
        print("You Pressed Enter!")
        
    def running(self):
        print("new login started")


if __name__ == "__main__":
    app = newlogin(None)
    app.mainloop()
