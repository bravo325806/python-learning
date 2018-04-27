import npyscreen

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Hello World!")

class MainForm(npyscreen.ActionForm):
    # Constructor
    def create(self):
        # Add the TitleText widget to the form
        self.title = self.add(npyscreen.TitleText, name="TitleText", value="Hello Plusone")
        y, x = self.useable_space()
        print(x,y)
        self.add(npyscreen.TitleDateCombo, name="Date:", max_width=int(x//2).min_width=int(x//2) )

    # Override method that triggers when you click the "ok"
    def on_ok(self):
        self.parentApp.setNextForm(None)
    # Override method that triggers when you click the "cancel"
    def on_cancel(self):
        self.title.value = "Hello World!"
if __name__ == '__main__':
    MyApp = App()
    MyApp.run()
