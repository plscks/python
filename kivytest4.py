# KIVY TEST 4!
# READY FOR ANOTHER FAILURE?!
# YES PLEASE
##
# written by plscks
import kivy

from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class PongApp(App):

    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongApp().run()
