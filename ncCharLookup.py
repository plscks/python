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
# [] Use Tkinter to make a GUI that is cross compatable
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
# Following this Tkinter guide https://www.python-course.eu/tkinter_entry_widgets.php
#
# ONWARDS!!
import tkinter as tk


def testing(text):
    print('Button clicked!')
    print(text)


root = tk.Tk()
root.title('Counting Seconds')
fieldName = tk.Label(root, text='Character Name: ').grid(row=2, column=0)
charName = tk.StringVar()
e1 = tk.Entry(root, textvariable=charName).grid(row=2, column=1)
button = tk.Button(root, text='Lookup', width=20, command=lambda: testing(charName.get()))
button.grid(row=2, column=2)
exit = tk.Button(root, text='QUIT', width=20, command=root.destroy).grid(row=3, column=1)
root.mainloop()
