
import pymongo
from pymongo import MongoClient
import smaillproject_todo 
from datetime import datetime
import webbrowser,requests,bs4
myClinet = MongoClient()
db = myClinet["todo_list"] # db name
job_list = db["todo_data"]  # collections

class dataProcess(object):
    def __init__(self,job,time):
        self.job = job
        self.time = time
    def add_data():
        job = smaillproject_todo.jobName
        time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        wantto_add = {
            "wantDo":job,
            "add_time":time,
            "if_finish":'undone' }
        job_list.insert_one(wantto_add).inserted_id
    def del_data():
        job = str(smaillproject_todo.jobName)
        want_del = job_list.remove({"wantDo":job})
        if(want_del['n']>0):
            print('Delete', job , 'successfully')
        else:
            print('Not found',job)
    def work_done():
        job = str(smaillproject_todo.jobName)
        job_done = job_list.update(
            {"wantDo":job},
            {'$set':{"if_finish":"done"}}
        )
        if(job_done['n']>0):
            print('The', job , 'has been done')
        else:
            print('Not found',job)
    def show_list():
        print("\033[90m┌────────────┬──────────────────┬─────────────┬──────────┬────────┐") 
        print("│\033[96m id \033[0m        \033[90m│ \033[96mjob\033[0m              \033[90m│ \033[96mdate\033[0m        \033[90m│ \033[96mtime\033[0m     \033[90m│ \033[96mfinish\033[0m \033[90m│")
        print("\033[90m├────────────┼──────────────────┼─────────────┼──────────┼────────┤") 
        count = 1
        for todo in job_list.find(): 
            print("│"+str(todo['_id'])[0:10]+"  │ \033[93m"+'{:16}'.format(todo['wantDo'][0:15]) +"\033[90m │ "+todo['add_time'][0:11]+" │ "+todo['add_time'][11:20]+" │ \033[91m"+'{:7}'.format(todo['if_finish'])+"\033[90m│")
            if count == job_list.find().count():print("└────────────┴──────────────────┴─────────────┴──────────┴────────┘\033[0m")
            else:print("├────────────┼──────────────────┼─────────────┼──────────┼────────┤") 
            count = count +1 
    def google_map():
        address = smaillproject_todo.jobName
        webbrowser.open('https://www.google.com/maps/place/'+address)
    
    def google_search():
        search_item = smaillproject_todo.jobName
        res = requests.get('https://www.google.com/search?q='+' '.join(search_item))
        soup = bs4.BeautifulSoup(res.text,"html5lib")
        linkElems = soup.select('.r a') # <h3 class="r">  <a> elments
        openNum = min(5,len(linkElems)) #open number 5
        for i in range(openNum):
            webbrowser.open('http://google.com'+linkElems[i].get('href'))