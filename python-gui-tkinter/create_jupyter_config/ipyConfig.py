def congfig_setting(pswHash,f):
    
    ip = "c.NotebookApp.ip ='*'" 
    browser = "c.NotebookApp.open_browser = False"
    password = "c.NotebookApp.password =" +"\'"+ str(pswHash)+"\'"
    f.write(ip +"\n"+ browser + "\n" + password )
    print(ip +"\n"+ browser + "\n" + password )
    