'''Need to set the close parameter

    adds:
    1 New player'''

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from pyConnect import *
from newlogin import *

# from http://effbot.org/tkinterbook/entry.htm
dataB = pyConnect()
failure_max = 3

def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
def enter(event):
    check_password()
    
def check_password():
    """ Collect 1's for every failure and quit program in case of failure_max failures """
    print(user.get(), password.get())
    passwords = dataB.get_login(user.get())
    print(passwords)
    for p in passwords:
        if (p[2] == password.get()):
            print('Logged in')
            check_password.user = user.get()
            root.destroy()
            print('Logged in')
            return
        
    check_password.failures += 1
    if check_password.failures == failure_max:
        root.destroy()
        raise SystemExit('Unauthorized login attempt')
    else:
        root.title('Try again. Attempt %i/%i' % (check_password.failures + 1, failure_max))


def new_account():
    
    print("Starting New Account")
    
    nlog = newlogin(None)
    #nlog.running()


        
check_password.failures = 0
root = tk.Tk()
root.geometry('300x160')
root.title('Please Login')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#entrys with not shown text
user = make_entry(parent, "User name:", 16)
password = make_entry(parent, "Password:", 16, show="*")
#button to attempt to login
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=8, command=check_password)
b2 = tk.Button(parent, borderwidth=4, text="New", width=10, pady=8, command=new_account)
b.pack(side=tk.RIGHT)
b2.pack(side=tk.RIGHT)
password.bind('<Return>', enter)
user.focus_set()
parent.mainloop()
