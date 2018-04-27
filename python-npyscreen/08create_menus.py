

import npyscreen
class FormObj(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):
	def create(self):
		self.fname = self.add( npyscreen.TitleText, name= 'Name:', value= 'plusone')
		self.add(npyscreen.TitleText, name='bithday', value="18/2/22")
		# menus 	
		self.menu = self.new_menu(name = 'Main Menu', shortcut ='m')
		self.menu.addItem(text='Item 1', onSelect=self.press_1, shortcut='1')
		self.menu.addItem(text='Item 2',  onSelect=self.press_2, shortcut='2')
		self.menu.addItem(text='Exit Form',  onSelect= self.exit_form, shortcut='^x')
		# submenu
		self.submenu = self.menu.addNewSubmenu('A new Menu')	
		self.submenu.addItem("This is submenu")
	def press_1(self):
		npyscreen.notify_confirm("You pressed Item 1")
	def press_2(self):
                npyscreen.notify_confirm("You pressed Item 2")
	def exit_form(self):
		self.parentApp.switchForm(None)
	
	def on_ok(self):
		# ok btn press
		npyscreen.notify_confirm('Form has been saved!', editw=1)
		self.parentApp.setNextForm(None)
	def on_cancel(self):
		# cancel btn press
		if_exit = npyscreen.notify_yes_no('Are you sure want to cancel?','Postive?', editw=1)
		if (if_exit):
			npyscreen.notify_confirm("Form has NOT saved!", 'BYE BYE')
			self.parentApp.setNextForm(None)
		else:
			npyscreen.notify_confirm("You may continue working", 'OKAY!')
class App(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', FormObj, name='hello-world', lines=10) 


if __name__ == '__main__':
	app = App()
	app.run()
