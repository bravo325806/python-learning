import json
from notebook.auth import passwd
import os

jupyter = "jupyter_notebook_config"
nowUserPort = "8000" 

# loading json file
def load_json_file():
    json_d = open('d.json')
    global data 
    data = json.load(json_d)
    print(data)
    return data

def find_user_port(nowUserPort):
    usedPortList = []
    for _id in data['users']:
        usedPortList.append(_id['port'])
        # usedPortList.sort()
    for used in usedPortList:
        if nowUserPort in usedPortList:
            nowUserPort = int(nowUserPort) +1 
            print("now:",nowUserPort)
            nowUserPort = str(nowUserPort)
        else:
            nowUserPort = str(nowUserPort)
    print("now user's port:", nowUserPort)
    return nowUserPort

def congfig_setting(hashpwd,fileName,nowPort,data,f):
    _id = fileName
    newData = {
        "id":_id,
        "port":nowPort
    }
    print("new data:",newData)
    data["users"].append(newData)
    ip = "c.NotebookApp.ip ='*'" 
    browser = "c.NotebookApp.open_browser = False"
    port = "c.NotebookApp.port =" + str(nowPort)
    password = "c.NotebookApp.password =" +"\'"+ str(hashpwd)+"\'"
    f.write(ip +"\n"+ browser + "\n" + password +"\n" + port)
    
    print(ip +"\n"+ browser + "\n" + password + "\n"+ port)
    d = open('./d.json', "w+")                
    data = str(data).replace("'", "\"")
    d.write(data)
    print("save!")


print('please enter your user ID:')
userId = input()
fileName = userId
print('please enter your user Password:')
psw = input()
hashpwd = passwd(psw)



if os.path.exists(jupyter+"_"+fileName+".py"):
        print(userId + "EXISTS")
else:
    with open(jupyter+"_"+fileName+".py","wt") as f: 
        load_json_file()
        nowPort =  find_user_port(nowUserPort)                
        congfig_setting(hashpwd,fileName,nowPort,data,f)