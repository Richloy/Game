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
        
        self.dataB = pyConnect() 
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry('300x200')
        self.title('Login')

        self.label_variable = tk.StringVar()
        self.label = tk.Label(self, textvariable = self.label_variable,
                              anchor = "w", fg = "blue")
        self.label_variable.set("")
        self.label.pack()
        self.login()
        #self.user_credentials()

    def login(self):
        
        #create frame
        self.login_frame = ttk.Labelframe(self, text = 'Login Details')
        self.login_frame.pack()
        self.grid()

        #Username
        self.user_label = tk.Label(self.login_frame, text = "Username", fg = "red")
        self.user_label.grid(column = 0, row = 0)

        self.user_entry_variable = tk.StringVar()
        self.user_entry = tk.Entry(self.login_frame, textvariable = self.user_entry_variable, fg = "brown")
        self.user_entry.grid(column = 1, row = 0)

        seperator = tk.Label(self.login_frame, text = "")
        seperator.grid(column = 0, row = 1, sticky = 'EW')

        #Password
        self.user_pwd_label = tk.Label(self.login_frame, text = "Password", fg = "red")
        self.user_pwd_label.grid(column = 0, row = 2, sticky = 'EW')

        self.user_pwd_variable = tk.StringVar()
        self.user_pwd_entry = tk.Entry(self.login_frame, textvariable = self.user_pwd_variable, fg = "brown")
        self.user_pwd_entry.grid(column = 1, row = 2)

        self.button = tk.Button(self.login_frame,text = "Login", command = self.check_password)
        self.button.grid(column = 1,row = 3, sticky = 'E')
        
        self.button = tk.Button(self.login_frame,text = "New Account", command = self.on_Button_Click)
        self.button.grid(column = 2, row = 3)
        
        #self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.user_entry.focus_set()
        self.user_entry.selection_range(0, tk.END)

    def user_credentials(self):
        self.create_frame = ttk.Labelframe(self, text = 'Credentials', borderwidth = 5)
        self.create_frame.pack()
        self.grid()
        
        self.user_label = tk.Label(self.create_frame, text="Username", fg="red")
        self.user_label.grid(column=0, row=0)

        self.user_entry_variable = tk.StringVar()
        self.user_entry = tk.Entry(self.create_frame, textvariable = self.user_entry_variable, fg="brown")
        self.user_entry.grid(column=1, row=0)

        seperator = tk.Label(self.create_frame, text="")
        seperator.grid(column=0, row=1, sticky='EW')
        
        self.user_pwd_label = tk.Label(self.create_frame, text="Password", fg="red")
        self.user_pwd_label.grid(column=0, row=2, sticky='EW')

        self.user_pwd_variable = tk.StringVar()
        self.user_pwd_entry = tk.Entry(self.create_frame, textvariable = self.user_pwd_variable, fg="brown")
        self.user_pwd_entry.grid(column=1, row=2)

        '''self.entry_variable = tk.StringVar()
        self.entry = tk.Entry(self.frame1, textvariable = self.entry_variable)
        self.entry.bind("<Return>", self.on_Press_Enter)
        self.entry.pack(anchor=tk.W)

        self.password_variable = tk.StringVar()
        self.password = tk.Entry(self.frame1, textvariable = self.password_variable)
        self.password.bind("<Return>", self.on_Press_Enter)
        self.password.pack()'''
        
        self.button = tk.Button(self.create_frame,text=u"Gender ->", command = self.on_Button_Click)
        self.button.grid(column=1,row=3)
        
        #self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.user_entry.focus_set()
        self.user_entry.selection_range(0, tk.END)

    def user_gender(self):
        print("Select Gender")
        self.gender_frame = ttk.Labelframe(self, text = 'Select Gender')
        self.gender_frame.pack()
        self.grid()
        v = tk.IntVar()
        
        self.gender_radio1 = tk.Radiobutton(self.gender_frame, text = "Male", variable = v, value = 0, width = 25, indicatoron = 0)
        self.gender_radio1.grid(column=0, row=0, columnspan = 2, sticky = 'W')

        self.gender_radio2 = tk.Radiobutton(self.gender_frame, text = "Female", variable = v, value = 1, width = 25, indicatoron = 0)
        self.gender_radio2.grid(column=0, row=1, columnspan = 2, sticky = 'W')
        self.update()

        seperator = tk.Label(self.gender_frame, text = "")
        #redbutton.pack(anchor = tk.NW)
        seperator.grid(column = 0, row = 2, sticky =' EW')
        
        self.gender_button = tk.Button(self.gender_frame,text=u"Skin Colour ->", command = self.on_gender_button_click)
        self.gender_button.grid(column=1,row=3)
        self.gender_back_button = tk.Button(self.gender_frame,text=u"<- Back", command = self.on_gender_back_button_click)
        self.gender_back_button.grid(column = 0,row = 3, sticky = 'E')

    def check_password(self):
        print(self.user_entry_variable.get(), self.user_pwd_variable.get())
        passwords = self.dataB.get_login(self.user_entry_variable.get())
        print(passwords)
        for p in passwords:
            if (p[2] == self.user_pwd_variable.get()):
                print('Logged in')
                #check_password.user = self.user_entry_variable.get()
                app.destroy()
                print('Logged in')
                return
            
    def on_Button_Click(self):

        self.label_variable.set("Welcome " + self.user_entry_variable.get())
        self.user_entry.focus_set()
        self.user_entry.selection_range(0, tk.END)
        print("You Clicked!")
        print(self.user_entry_variable.get())
        print(self.user_pwd_variable.get())
        self.create_frame.destroy()
        self.user_gender()

    def on_gender_button_click(self):
        pass

    def on_gender_back_button_click(self):
        self.gender_frame.destroy()
        self.user_credentials()
        
    def on_Press_Enter(self, event):

        self.label_variable.set("Welcome " + self.entry_variable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)
        print("You Pressed Enter!")
        
    def running(self):
        print("new login started")


#if __name__ == "__main__":
app = newlogin(None)
app.mainloop()
