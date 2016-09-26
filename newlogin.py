''' Login Using Frames
    Created Show Password Checkbox
    '''

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from pyConnect import *

class newlogin(tk.Tk):
    
    def __init__(self, parent):

        self.login_try = 0
        self.dataB = pyConnect() 
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry('300x200')
        self.title('Login')
        self.password_failure_max = 3
        self.password_failures = 0

        self.label_variable = tk.StringVar()
        self.label = tk.Label(self, textvariable = self.label_variable,
                              anchor = "w", fg = "blue")
        self.label_variable.set("")
        self.label.pack()
        self.login()

    def login(self):
        
        #create frame
        self.login_frame = ttk.Labelframe(self, text = 'Login Details')
        self.login_frame.pack()
        self.label_variable.set("")
        self.checked = tk.IntVar()
        self.grid()

        #Username
        self.user_label = tk.Label(self.login_frame, text = "Username", fg = "red")
        self.user_label.grid(column = 0, row = 0)

        self.user_entry_variable = tk.StringVar()
        self.user_entry = tk.Entry(self.login_frame,
                                   textvariable = self.user_entry_variable,
                                   fg = "brown")
        self.user_entry.grid(column = 1, row = 0)

        seperator = tk.Label(self.login_frame, text = "")
        seperator.grid(column = 0, row = 1, sticky = 'EW')

        #Password
        self.user_pwd_label = tk.Label(self.login_frame, text = "Password",
                                       fg = "red")
        self.user_pwd_label.grid(column = 0, row = 2, sticky = 'EW')

        self.user_pwd_variable = tk.StringVar()
        self.user_pwd_entry = tk.Entry(self.login_frame,
                                       textvariable = self.user_pwd_variable,
                                       fg = "brown", show = "*")
        self.user_pwd_entry.grid(column = 1, row = 2)

        #Buttons
        self.button_login = tk.Button(self.login_frame,text = "Login",
                                      command = self.check_password)
        self.button_login.grid(column = 1,row = 4, sticky = 'E')
        
        self.button_new = tk.Button(self.login_frame,text = "New Account",
                                    command = self.new_acc_click)
        self.button_new.grid(column = 2, row = 4)

        #Password show checkbox
        self.pass_radio1 = tk.Checkbutton(self.login_frame, text = "Show Password",
                                          variable = self.checked, width = 25,
                                          command = self.show_pass)
        self.pass_radio1.grid(column = 0, row = 3, columnspan = 2, sticky = 'W')
        
        #self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.user_entry.focus_set()
        self.user_entry.selection_range(0, tk.END)

    def user_credentials(self):

        #Create Frame
        self.create_frame = ttk.Labelframe(self, text = 'Credentials', borderwidth = 5)
        self.create_frame.pack()
        self.checked = tk.IntVar()
        self.grid()

        #Username
        self.user_label = tk.Label(self.create_frame, text = "Username", fg = "red")
        self.user_label.grid(column = 0, row = 0)

        self.user_entry_variable = tk.StringVar()
        self.user_entry = tk.Entry(self.create_frame,
                                   textvariable = self.user_entry_variable,
                                   fg = "brown")
        self.user_entry.grid(column = 1, row = 0)

        seperator = tk.Label(self.create_frame, text = "")
        seperator.grid(column = 0, row = 1, sticky = 'EW')

        #Password
        self.user_pwd_label = tk.Label(self.create_frame, text = "Password",
                                       fg = "red")
        self.user_pwd_label.grid(column = 0, row = 2, sticky = 'EW')

        self.user_pwd_variable = tk.StringVar()
        self.user_pwd_entry = tk.Entry(self.create_frame,
                                       textvariable = self.user_pwd_variable,
                                       fg = "brown", show = "*")
        self.user_pwd_entry.grid(column = 1, row = 2)

        #Password show checkbox
        self.pass_radio2 = tk.Checkbutton(self.create_frame,
                                          text = "Show Password",
                                          variable = self.checked, width = 25,
                                          command = self.show_pass)
        self.pass_radio2.grid(column = 0, row = 3, columnspan = 2, sticky = 'W')

        #Buttons        
        self.button_check = tk.Button(self.create_frame,text = "Check",
                                      command = self.check_username)
        self.button_check.grid(column = 2, row = 0)
        
        self.button_back = tk.Button(self.create_frame,text = "<- Login",
                                     command = self.cred_back_click)
        self.button_back.grid(column = 1, row = 4, sticky = 'E')
        
        self.button_forward = tk.Button(self.create_frame,text = "Gender ->",
                                        command = self.cred_forward_click)
        self.button_forward.grid(column = 2, row = 4)
        
        self.update()
        self.geometry(self.geometry())
        self.user_entry.focus_set()
        self.user_entry.selection_range(0, tk.END)

    def user_gender(self):
        
        print("Select Gender")
        self.gender_frame = ttk.Labelframe(self, text = 'Select Gender')
        self.gender_frame.pack()
        self.gender = tk.IntVar()
        self.grid()
        
        self.gender_radio1 = tk.Radiobutton(self.gender_frame,
                                            text = "Male", variable = self.gender,
                                            value = 0, width = 25, indicatoron = 0)
        self.gender_radio1.grid(column = 0, row = 0, columnspan = 2, sticky = 'W')

        self.gender_radio2 = tk.Radiobutton(self.gender_frame,
                                            text = "Female", variable = self.gender,
                                            value = 1, width = 25, indicatoron = 0)
        self.gender_radio2.grid(column = 0, row = 1, columnspan = 2, sticky = 'W')
        self.update()

        seperator = tk.Label(self.gender_frame, text = "")
        #redbutton.pack(anchor = tk.NW)
        seperator.grid(column = 0, row = 2, sticky =' EW')
        
        self.gender_button = tk.Button(self.gender_frame, text = "Skin Colour ->",
                                       command = self.gender_forward_click)
        self.gender_button.grid(column = 1, row = 3)
        self.gender_back_button = tk.Button(self.gender_frame, text = "<- Back",
                                            command = self.gender_back_click)
        self.gender_back_button.grid(column = 0, row = 3, sticky = 'E')

    def skin_colour(self):

        self.colour_frame = ttk.Labelframe(self, text = 'Select Skin Tone')
        self.colour_frame.pack()
        self.skin_tone = tk.IntVar()
        self.image1 = tk.PhotoImage(file = ".\images\\col1.png")
        self.image2 = tk.PhotoImage(file = ".\images\\col2.png")
        self.image3 = tk.PhotoImage(file = ".\images\\col3.png")
        self.image4 = tk.PhotoImage(file = ".\images\\col4.png")
        self.grid()
        
        self.gender_radio1 = tk.Radiobutton(self.colour_frame,
                                            image = self.image1,
                                            variable = self.skin_tone,
                                            value = 0, width = 40, height = 40,
                                            indicatoron = 0)
        self.gender_radio1.grid(column = 0, row = 0, columnspan = 2, sticky = 'W')

        self.gender_radio2 = tk.Radiobutton(self.colour_frame,
                                            image = self.image2,
                                            variable = self.skin_tone,
                                            value = 1, width = 40, height = 40,
                                            indicatoron = 0)
        self.gender_radio2.grid(column = 1, row = 0, columnspan = 2, sticky = 'W')
        
        self.gender_radio3 = tk.Radiobutton(self.colour_frame,
                                            image = self.image3,
                                            variable = self.skin_tone,
                                            value = 3, width = 40, height = 40,
                                            indicatoron = 0)
        self.gender_radio3.grid(column = 0, row = 1, columnspan = 2, sticky = 'W')

        self.gender_radio4 = tk.Radiobutton(self.colour_frame,
                                            image = self.image4,
                                            variable = self.skin_tone,
                                            value = 4, width = 40, height = 40,
                                            indicatoron = 0)
        
        self.gender_radio4.grid(column = 1, row = 1, columnspan = 2, sticky = 'W')
        self.update()

        seperator = tk.Label(self.colour_frame, text = "")
        seperator.grid(column = 0, row = 2, sticky =' EW')
        
        self.gender_button = tk.Button(self.colour_frame, text = "Submit ->",
                                       command = self.colour_forward_click)
        self.gender_button.grid(column = 1, row = 3)
        self.gender_back_button = tk.Button(self.colour_frame, text = "<- Back",
                                            command = self.colour_back_click)
        self.gender_back_button.grid(column = 0, row = 3, sticky = 'E')
        
    def check_password(self):
        print(self.user_entry_variable.get(), self.user_pwd_variable.get())
        passwords = self.dataB.get_login(self.user_entry_variable.get())
        print(passwords)
        for p in passwords:
            if (p[2] == self.user_pwd_variable.get()):
                print('Logged in')
                self.login_try = 1
                self.destroy()
                print('Logged in')
                return
        self.password_failures += 1
        if self.password_failures == self.password_failure_max:
            self.destroy()
            raise SystemExit('Unauthorized login attempt')
        else:
            self.title('Try again. Attempt %i/%i' % (self.password_failures + 1,
                                                     self.password_failure_max))
    def create_new_acc(self):

        print("Connecting to DB")
        self.destroy()
    
    def show_pass(self):

        if (self.checked.get()):
            self.user_pwd_entry.config(show = '')
        else:
            self.user_pwd_entry.config(show = "*")
            
    def new_acc_click(self):
        
        self.login_frame.destroy()
        self.user_credentials()

    def cred_back_click(self):
        
        self.create_frame.destroy()
        self.login()
        
    def cred_forward_click(self):
        
        print(self.user_entry_variable.get())
        used = self.dataB.check_new_username(self.user_entry_variable.get())
        if used:
            self.label_variable.set(self.user_entry_variable.get() +
                                    " Is in use, Please choose another Username")
        else:
            self.label_variable.set("")
            self.create_frame.destroy()
            self.user_gender()

    def check_username(self):

        used = self.dataB.check_new_username(self.user_entry_variable.get())
        if used:
            print("Name in Use")
            self.label_variable.set(self.user_entry_variable.get() +
                                    " Is in use, Please choose another Username")
        else:
            print("Name not in Use")
            self.label_variable.set(self.user_entry_variable.get() + " Is Available")
            
    def gender_forward_click(self):
        
        print(self.gender.get())
        self.gender_frame.destroy()
        self.skin_colour()

    def gender_back_click(self):
        
        self.gender_frame.destroy()
        self.user_credentials()
                    
    def colour_forward_click(self):
        
        print(self.skin_tone.get())
        self.colour_frame.destroy()
        self.create_new_acc()

    def colour_back_click(self):

        self.colour_frame.destroy()
        self.user_gender()

if __name__ == "__main__":
    app = newlogin(None)
    app.mainloop()
