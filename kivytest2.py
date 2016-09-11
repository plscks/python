## This has been a complete failure.
## written my plscks

#import kivy
#kivy.require('1.9.1')

#from kivy.app import App
#from kivy.uix.button import Button
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label

#class LoginScreen(GridLayout):
#    def __init__(self, **kwargs):
#        self.add_widget(Label(text='FUCK!')

#class Stuff(GridLayout):
#    def __init__(self, **kwargs):
#        #super(Stuff, self).__init__(**kwargs)
#        self.add_widget(Button(text='Oh Jesus?')

#class MyApp(App):

#    def build(self):
#        return Stuff()

#if __name__ == '__main__':
#    MyApp().run()

#class MyApp(App):

#    def build(self):
#        return LoginScreen()

#if __name__ == '__main__':
#    MyApp().run()


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Stuff(Button):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        #self.cols = 2
        self.add_widget(Label(text='FUCK FUCK FUCK!'))
        #self.username = TextInput(multiline=False)
        #self.add_widget(Label(text='Passphrase: '))
        #self.password = TextInput(password=True, multiline=False)
        #self.add_widget(self.password)

class MyApp(App):

    def build(self):
        return Stuff()

if __name__ == '__main__':
    MyApp().run()
