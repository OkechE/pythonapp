import tkinter as tk
from tkinter import messagebox, Text

root = tk.Tk()

def hi():

    hello = messagebox.showinfo(title='hello world', message='hellohhhh')
    print = hello

canvas = tk.Canvas(root, height=700, width= 700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

pressMe = tk.Button(root, text="press me", padx= 10, 
                    pady=5, fg="black", bg="black", command=hi)
pressMe.pack()

root.mainloop()