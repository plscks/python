#!/usr/bin/python3
# Nexus Clash character profile info lookup by name
# Version 2.0
# Written by plscks
#
# Let's see if I can get this thing to work well
# Let's see if I can get this thing to work at all?!
# Is this a test, it has to be.....
#
#################
## TO DO LIST  ##
#################
# [x] Use Tkinter to make a GUI that is cross compatable
# [X] Hook into NC charater profile API
# [X] Have a text field to type a name
# [X] Lookup data and get json
# [X] Parse json into readable format and display in copy/pastable format
# [] Actually show faction name
# [X] Actually show avatar
# [] List how many exploration badges they have and how many remain to be gotten
# [] List which stat grinds they have completed
# [x] write program like a real program and not in dumb testing segments
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
from PIL import ImageTk,Image
import requests
import tkinter as tk
from urllib.request import urlopen
from io import BytesIO
import webbrowser


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid_forget()

        # Setting default buttons and fields
        charName = tk.StringVar()
        queryNameLabel = tk.Label(self, text='Check Character Name: ')
        queryNameLabel.grid(row=2, column=0)
        queryEntryField = tk.Entry(self, textvariable=charName)
        queryEntryField.grid(row=2, column=1)
        adStatusField = tk.Label(self, text='', width=40)
        adStatusField.grid(row=3, column=1, columnspan=1)
        lookupBtn = tk.Button(self, text='Lookup', width=6, command=lambda: self.infoGather(charName.get(), adStatusField))
        lookupBtn.grid(row=2, column=2, pady=10)
        exit = tk.Button(self, text='QUIT', width=20, command=root.destroy)
        exit.grid(row=18, column=2, padx=10, pady=10)
        self.gridInit()


    def gridInit(self):
        # Create buttons
        avatarField = tk.Canvas(self, width = 250, height = 250)
        charNameLabel = tk.Label(self, text='Character Name: ')
        charNamePanel = tk.Entry(self, state='readonly', readonlybackground='white', fg='black', width=25)
        charIDLabel = tk.Label(self, text='Character ID: ')
        charIDPanel = tk.Entry(self, state='readonly', readonlybackground='white', fg='black', width=25)
        profileBtn = tk.Label(self, text="profile", fg="blue", cursor="hand2")
        charClassInfoLabel = tk.Label(self, text='Character Level & Class')
        charClassInfoPanel = tk.Entry(self, state='readonly', readonlybackground='white', fg='black', width=25)


        # Position of buttons
        avatarField.grid(row=4, rowspan=15, column=0)
        charNameLabel.grid(row=4, column=1, sticky=tk.E)
        charNamePanel.grid(row=4, column=2, columnspan=2)
        charIDLabel.grid(row=5, column=1, sticky=tk.E)
        charIDPanel.grid(row=5, column=2, columnspan=2)
        charClassInfoLabel.grid(row=6, column=1, sticky=tk.E)
        charClassInfoPanel.grid(row=6, column=2, columnspan=3)
        profileBtn.grid(row=3, column=2)


    def infoGather(self, inName, status):
        inName.replace(' ', '%20')
        response = requests.get('https://www.nexusclash.com/modules.php?name=Character&charname=' + str(inName) + '&format=json')
        data = response.json()

        tk.Label(self, text='Character Name: ').grid(row=4, column=1, sticky=tk.E)
        collectedName = tk.StringVar()
        collectedName.set(data['result']['character']['name']['name'])
        charNamePanel = tk.Entry(self, state='readonly', readonlybackground='white', fg='black', width=25)
        charNamePanel.config(textvariable=collectedName, relief='flat')
        charNamePanel.grid(row=4, column=2, columnspan=2)

        tk.Label(self, text='Character ID: ').grid(row=5, column=1, sticky=tk.E)
        collectedID = tk.StringVar()
        collectedID.set(data['result']['character']['id'])
        charIDPanel = tk.Entry(self, state='readonly', readonlybackground='white', fg='black', width=25)
        charIDPanel.config(textvariable=collectedID, relief='flat')
        charIDPanel.grid(row=5, column=2, columnspan=2)

        profileBtn = tk.Label(self, text="profile", fg="blue", cursor="hand2")
        profileBtn.bind('<Button-1>', lambda e: self.callback('https://www.nexusclash.com/modules.php?name=Game&op=character&id=' + str(data['result']['character']['id'])))
        profileBtn.grid(row=3, column=2)

        try:
            URL = data['result']['character']['avatar']['url'].replace(' ', '%20')
            u = urlopen(URL)
        except:
            URL = 'https://github.com/plscks/python/raw/master/nochar.png'
            u = urlopen(URL)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        if im.width <= 250:
            pass
        else:
            im = im.resize((240, 240), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        avatar = tk.Canvas(self, width = 250, height = 250)
        avatar.image = photo
        avatar.create_image(5, 127, anchor=tk.W, image=photo)
        avatar.grid(row=3, rowspan=15, column=0)

        if data['result']['character']['status']['alive'] == True:
            status.config(text='This character is currently alive.')
        else:
            status.config(text='This character is floating above the planes.')
        if data['result']['character']['id'] == 0:
            status.config(text='No character exists with this name.')

        charClass = charClass = len(data['result']['character']['classes']) - 1
        collectedLevel = str(data['result']['character']['level'])
        collectedClass = data['result']['character']['classes'][charClass]
        collectedClassInfo = tk.StringVar()
        collectedClassInfo.set('Level ' + collectedLevel + ' ' + collectedClass)
        charClassInfoLabel = tk.Label(self, text='Character Level & Class')
        charClassInfoPanel = tk.Entry(self, state='readonly', readonlybackground='white', fg='black', width=25)
        charClassInfoLabel.grid(row=6, column=1, sticky=tk.E)
        charClassInfoPanel.config(textvariable=collectedClassInfo, relief='flat')
        charClassInfoPanel.grid(row=6, column=2, columnspan=3)


    def callback(self, url):
        webbrowser.open_new(url)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Nexus Clash Character Profile Lookup')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
