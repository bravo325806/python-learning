import tkinter as tk
from notebook.auth import passwd
import os
from ipyConfig import congfig_setting
window = tk.Tk()
window.title('Create Password')
window.geometry('300x200')
jupyter = "jupyter_notebook_config"

def hit_me():
    fileName = userId.get()
    psw = e.get()
    var.set('Create Password Successfully')  # gui show  
    hashpwd = passwd(psw)
    if os.path.exists(jupyter+"_"+fileName+".py"):
            var.set('User have Exists!')
    else:
        with open(jupyter+"_"+fileName+".py","wt") as f:                 
            congfig_setting(hashpwd,f)
l = tk.Label(window, 
    text='User Id',
    font=('Arial', 12), 
    width=30, height=2
    )
l.pack() 
userId = tk.Entry(window)
userId.pack()

l = tk.Label(window, 
    text='Please Enter Password',
    font=('Arial', 12), 
    width=30, height=2
    )
l.pack()    

e = tk.Entry(window,show='*',)
e.pack()

var = tk.StringVar()   
l = tk.Label(window, 
             textvariable=var,  
             font=('Arial', 12), width=30, height=2)
l.pack() 
b = tk.Button(window, 
              text='Create Password', 
              width=15, height=2, 
              command=hit_me)   
b.pack() 

window.mainloop()