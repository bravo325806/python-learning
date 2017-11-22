import sys,pyperclip
# import class
from todo_model import dataProcess as todo
def funSwitch():
    if funcChoose == 'del': todo.del_data()
    elif funcChoose == 'add': todo.add_data()
    elif funcChoose == 'done': todo.work_done()
    elif funcChoose == 'show': todo.show_list()
if len(sys.argv)>1:
    funcChoose = ''.join(sys.argv[1:2])
    jobName = ' '.join(sys.argv[2:])
    funSwitch()      
else:
    print('what do you want to do ? del,add or done ?')
    funcChoose = input()
    print(funcChoose , 'which job ?' )
    jobName = input()
    funSwitch()
   
