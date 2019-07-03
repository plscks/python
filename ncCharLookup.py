#!/usr/bin/python3
# Nexus Clash character profile info lookup by name
# Written by plscks
#
# Let's see if I can get this thing to work well
# Let's see if I can get this thing to work at all?!
# Is this a test, it has to be.....
#
#################
## TO DO LIST  ##
#################
# [] Use Kivy to make a GUI that is cross compatable
# [] Hook into NC charater profile API
# [] Have a text field to type a name
# [] Lookup data and get json
# [] Parse json into readable format and display in copy/pastable format
# [] Actually show faction name
# [] Actually show avatar
# [] List how many exploration badges they have and how many remain to be gotten
# [] List which stat grinds they have completed
# [] write program like a real program and not in dumb testing segments
# [] If need to do testing, clear it out and refactor
#
####################
##  HELPFUL LINKS ##
####################
# https://www.nexusclash.com
# https://www.nexusclash.com/modules.php?name=Character&charname=[NAME GOES HERE]&format=json
# ----> Uses '%20' as a space
# Following this kivy guide: https://kivy.org/doc/stable/guide/basic.html
# https://techwithtim.net/tutorials/kivy-tutorial/example-gui/
#
# ONWARDS!!
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass


class charlookup(App): # <- Main Class
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    charlookup().run()
