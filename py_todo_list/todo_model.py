
import pymongo
from pymongo import MongoClient
import smaillproject_todo as todoapi
from datetime import datetime

myClinet = MongoClient()
db = myClinet["todo_list"] # db name
job_list = db["todo_data"]  # collections
class dataProcess(object):
    def __init__(self,job,time,ifdone):
        self.job = job
        self.time = time
        self.ifdone = ifdone
    def add_data():
        job = todoapi.jobName
        time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        ifdone = 'undone'
        # data that want to insert
        wantto_add = {
            "wantDo":job,
            "add_time":time,
            "if_finish":ifdone 
        }
        # insert data to mongo 
        has_been_added = job_list.insert_one(wantto_add).inserted_id
        print('insert job:',job,'insert time: ',time,'state:'+ifdone)
    def del_data():
        job = str(todoapi.jobName)
        if job == 'all' or 'ALL':
            want_del = job_list.remove({})
        else:
            want_del = job_list.remove({"wantDo":job})
            if(want_del['n']>0):
                print('Delete', job , 'successfully')
            else:
                print('Not found',job)
    def work_done():
        job = str(todoapi.jobName)
        ifdone = 'done'
        # print(job,'have been',ifdone)
        job_done = job_list.update(
            {"wantDo":job},
            {'$set':{"if_finish":"done"}}
        )
        if(job_done['n']>0):
            print('The', job , 'has been done')
        else:
            print('Not found',job)
    def show_list():
        print("\033[90m┌────────────┬─────────────────┬─────────────┬──────────┬────────┐") 
        print("│\033[96m id \033[0m        \033[90m│ \033[96mjob\033[0m             \033[90m│ \033[96mdate\033[0m        \033[90m│ \033[96mtime\033[0m     \033[90m│ \033[96mfinish\033[0m \033[90m│")
        print("\033[90m├────────────┼─────────────────┼─────────────┼──────────┼────────┤") 
        count = 1
        for todo in job_list.find(): 
            print("│"+str(todo['_id'])[0:10]+"  │ \033[93m"+'{:15}'.format(todo['wantDo'][0:12]) +"\033[90m │ "+todo['add_time'][0:11]+" │ "+todo['add_time'][11:20]+" │ \033[91m"+'{:7}'.format(todo['if_finish'])+"\033[90m│")
            if count == job_list.find().count():
                print("└────────────┴─────────────────┴─────────────┴──────────┴────────┘\033[0m")
            else:
                print("├────────────┼─────────────────┼─────────────┼──────────┼────────┤") 
            count = count +1 
        # HEADER = '\033[95m'
        # OKBLUE = '\033[94m'
        # OKGREEN = '\033[92m'
        # WARNING = '\033[93m'
        # FAIL = '\033[91m'
        # ENDC = '\033[0m'
        # BOLD = '\033[1m'
        # UNDERLINE = '\033[4m'