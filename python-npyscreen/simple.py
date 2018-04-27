

import npyscreen
class FormObj(npyscreen.ActionForm):
	def create(self):
		self.fname = self.add( npyscreen.TitleText, name= 'Name:', value= 'plusone')
		self.add(npyscreen.TitleText, name='bithday', value="18/2/22")
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
