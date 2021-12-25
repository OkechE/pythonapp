from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('Good morning :)')

frame1 = Frame(root, bg='grey')
frame1.pack(expand=True, fill=BOTH)

button1 = Button(frame1, text='Hello')
button1.pack(side=BOTTOM)

root.mainloop()