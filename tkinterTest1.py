import tkinter as tk

counter = 0
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

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
