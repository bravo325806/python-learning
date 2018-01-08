import tkinter as tk

window = tk.Tk()
window.title('Create Password')
window.geometry('300x200')
beCreate = False  
def hit_me():
    global beCreate
    psw = e.get()
    if beCreate == False:  
        beCreate = True
        var.set('Create Password Successfully')   
        print(psw)
    else:      
        var.set('Password has been Created !!!!') 

l = tk.Label(window, 
    text='Please Enter Password',
    font=('Arial', 16), 
    width=30, height=3
    )
l.pack()    

e = tk.Entry(window,show='*',)
e.pack()

var = tk.StringVar()   
l = tk.Label(window, 
             textvariable=var,  
             font=('Arial', 16), width=30, height=3)
l.pack() 
b = tk.Button(window, 
              text='Create Password', 
              width=15, height=2, 
              command=hit_me)   
b.pack() 

window.mainloop()