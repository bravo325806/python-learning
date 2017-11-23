import sys,pyperclip
from todo_model import dataProcess as todo
def funSwitch():
    if funcChoose == 'del':
        todo.del_data()
        todo.show_list()
    elif funcChoose == 'add':
        todo.add_data()
        todo.show_list()
    elif funcChoose == 'done':
        todo.work_done()
        todo.show_list()
    elif funcChoose == 'show':
        todo.show_list()
    elif funcChoose == 'map':
        todo.google_map()
    elif funcChoose == 'search':
        todo.google_search()
if len(sys.argv)>1:
    funcChoose = ''.join(sys.argv[1:2])
    jobName = ' '.join(sys.argv[2:])
    funSwitch()     
else:
    print('what do you want to do ? \'del\',\'add\' or \'done\' job?')
    funcChoose = input()
    print(funcChoose , 'which job ?' )
    todo.show_list()
    jobName = input()
    funSwitch()
