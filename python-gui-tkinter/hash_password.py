import tkinter as tk
from notebook.auth import passwd

window = tk.Tk()
window.title('Create Password')
window.geometry('300x200')
beCreate = False  
def hit_me():
    global beCreate
    fileName = userId.get()
    print('user name:',fileName)
    psw = e.get()
    if beCreate == False:  
        beCreate = True
        var.set('Create Password Successfully')  # gui show  
        print('user password:',psw)
        hashpwd = passwd(psw)
        print('hash password:',hashpwd)
    else:      
        var.set('Password has been Created !!!!') # gui show
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