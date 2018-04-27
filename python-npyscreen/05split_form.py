

import npyscreen
class FormObj(npyscreen.SplitForm):
	def create(self):
		self.add( npyscreen.TitleText, name= 'Name:', value= 'plusone')
		self.nextrely +=1
		self.add(npyscreen.TitleText, name='bithday', value="18/2/22")
	def afterEditing(self):
		self.parentApp.setNextForm(None)

class App(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', FormObj, name='hello-world', lines=10, columns=40, draw_line_at = 7) 


if __name__ == '__main__':
	app = App()
	app.run()
	print('ok')
