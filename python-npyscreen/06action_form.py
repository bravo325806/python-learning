

import npyscreen
class FormObj(npyscreen.ActionForm):
	def create(self):
		self.fname = self.add( npyscreen.TitleText, name= 'Name:', value= 'plusone')
		self.add(npyscreen.TitleText, name='bithday', value="18/2/22")
	def afterEditing(self):
		pass
	#	self.parentApp.setNextForm(None)
	def on_ok(self):
		self.fname.value = 'ok button pressed!'
		# ok btn press
	def on_cancel(self):
		self.fname.value = 'cancle btn pressed!'
		# cancel btn press
class App(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', FormObj, name='hello-world', lines=10) 


if __name__ == '__main__':
	app = App()
	app.run()
	print('ok')
