#!/usr/bin/env python

import npyscreen
from datetime import datetime
import json, os
        

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parentApp.setNextForm(None)
        
class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

# no.1 page - write logs page
class WriteLogFormObj(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.SplitForm):
    def create(self):   
        y, x = self.useable_space()
        # Name
        #if be saved
        self.saved = self.add( npyscreen.TitleText, name= 'Save status:', value= 'NOT SAVE', editable = False, color='STANDOUT')
        self.nextrely +=2
        self.fname = self.add( npyscreen.TitleText, name= 'Your Name:', value= 'plusone', editable = False)
        # log time
        self.logTime = self.add(npyscreen.TitleText, name='Log Time:' ,value= datetime.now().strftime("%Y-%m-%d"))
        # self.logTime.value = datetime.now().strftime("%Y-%m-%d")
        self.nextrely +=1
        self.todayDone = self.add(InputBox, name="What are you doing today?", max_height=y //3 )
        self.problem = self.add(InputBox, name='Any Problem?')

        def  all_logs():
            self.parentApp.switchForm('SECOUND')
        self.menu = self.new_menu(name ='Menu' , shortcut ='^x')
        self.menu.addItem(text='All Logs', onSelect= all_logs, shortcut='1')
        self.menu.addItem(text='Exit Menu', shortcut='2')
    
    def on_ok(self):
        # ok btn press
        data = {
            'userName':self.fname.value,
            'todayDone':self.todayDone.value,
            'saveTime':self.logTime.value,
            'todayProblem':self.problem.value
        }
        if not os.path.exists('./logs/'):
            os.mkdir('./logs')
            with open( './logs/'+ self.logTime.value+'.json', 'w') as f: 
                json.dump(data, f)
        else:
            with open( './logs/'+ self.logTime.value+'.json', 'w') as f: 
                json.dump(data, f)
        npyscreen.notify_confirm('Good!'+ self.fname.value+ '\n\nYour log has been saved!\nNow click "Cancel" to leave! ')
        self.saved.value = 'Saved! at ' + datetime.now().strftime("%Y-%m-%d.%H:%M")
       
    def on_cancel(self):
        # cancel btn press
        if (self.saved.value == 'Saved!'):
            npyscreen.notify_wait('Okay! '+ self.fname.value+":\n\nyour log has been SAVED in your directory!\n\nSee You!", 'BYE BYE')
            self.parentApp.setNextForm(None)
        else:    
            postive_exit = npyscreen.notify_yes_no( 'HEY! '+ self.fname.value+ '"\nYou has NOT saved!\nAre you sure want to Cancel?','Postive?', editw=1)
            if (postive_exit):
                self.parentApp.setNextForm(None)
            else:
                npyscreen.notify_confirm("You may continue working", 'Allright!')

# no.2 page - show logs page
class ShowLogsForm(npyscreen.ActionForm, npyscreen.FormWithMenus):
    def create(self):   
        y, x = self.useable_space()
        self.add( npyscreen.TitleText, name= 'NOW:', value= datetime.now().strftime("%Y-%m-%d %H:%M"), editable = False)    

    def on_ok(self):
       pass
       
    def on_cancel(self):
        # cancel btn press
        self.parentApp.setNextForm('MAIN')



class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', WriteLogFormObj, draw_line_at = 4, name ='write_log') 
        self.addForm('SECOUND', ShowLogsForm, name ='show_logs') 

if __name__ == '__main__':
	app = App()
	app.run()
