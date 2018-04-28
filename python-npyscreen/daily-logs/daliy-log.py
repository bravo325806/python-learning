

import npyscreen
from datetime import datetime
import json, os
        
class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parentApp.setNextForm(None)
        
class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class FormObj(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.SplitForm):
    def create(self):   
        y, x = self.useable_space()
        # Name
        #if be saved
        self.saved = self.add( npyscreen.TitleText, name= 'Save status:', value= 'NOT SAVE', editable = False, color='STANDOUT')
        self.nextrely +=2
        self.fname = self.add( npyscreen.TitleText, name= 'Your Name:', value= 'plusone', editable = False)
        # log time
        self.logTime = self.add(npyscreen.TitleText, name='Log Time:' )
        self.logTime.value = datetime.now().strftime("%Y-%m-%d")
        self.nextrely +=1
        self.todayDone = self.add(InputBox, name="What are you doing today?", max_height=y //3 )
        self.problem = self.add(InputBox, name='Any Problem?')
        # menus 	
        def weekly_logs():
            npyscreen.notify_confirm('This function not completed yet')
        def  all_logs():
            npyscreen.notify_confirm('This function not completed yet')
        
        self.menu = self.new_menu(name ='Menu' , shortcut ='^x')
        self.menu.addItem(text='Weekly Logs', onSelect= weekly_logs, shortcut='1')
        self.menu.addItem(text='All Logs', onSelect= all_logs, shortcut='2')
        self.menu.addItem(text='Exit Menu', shortcut='3')
        
    def exit_form(self):
        self.parentApp.switchForm(None)
	
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
        npyscreen.notify_confirm('Good!'+ self.fname.value+ '\nYour log has been saved!\nNow click "Cancel" to leave! ')
        self.saved.value = 'Saved!'
       
    def on_cancel(self):
        # cancel btn press
        if (self.saved.value == 'Saved!'):
            npyscreen.notify_wait('OK! '+ self.fname.value+":\nyour log has been SAVED in your directory!\nSee you!", 'BYE BYE')
            self.parentApp.setNextForm(None)
        else:    
            if_exit = npyscreen.notify_yes_no( 'HEY! '+ self.fname.value+ '\nAre you sure want to Cancel?','Postive?', editw=1)
            if (if_exit):
                npyscreen.notify_confirm('oh....'+ self.fname.value +"\nyour log has NOT saved!", 'BYE BYE')
                self.parentApp.setNextForm(None)
            else:
                npyscreen.notify_confirm("You may continue working", 'Allright!')
        
class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObj, draw_line_at = 4, name ='DALIY LOGS') 
        

if __name__ == '__main__':
	app = App()
	app.run()
