

import npyscreen

class FormObj(npyscreen.Form):
	def create(self):
		self.add( npyscreen.TitleText, name= 'Name:', value= 'plusone')
		
	def afterEditing(self):
		self.parentApp.setNextForm(None)

class App(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', FormObj, name='hello-world') 


if __name__ == '__main__':
	app = App()
	app.run()
	print('ok')
