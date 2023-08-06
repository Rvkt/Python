from tkinter import *
from tkinter import ttk
import tkinter.font as font

root = Tk()
root.title('Palindrome Generator')

f = font.Font(family='Roboto Condensed', size=18, weight='bold')
f2 = font.Font(family='Varela Round', size=15, weight='bold')

frame = LabelFrame(root, text='Frame Title', pady=30, padx=30)
frame.grid(row=0, column=0, padx=30, pady=30)

e = Entry(frame, width=30, bg='#f2f2f2', borderwidth=2, font=f)
e.grid(row=0, column=0)
e.get()
e.delete(0, END)

def palindrome():
    global label
    txt1 = e.get()
    txt2 = txt1[-2::-1]
    join_txt = f'{txt1}{txt2}'
    result.config(text=join_txt)
    e.delete(0, END)

result = Label(frame, text='', font=f, fg='red')
result.grid(row=1, column=0, columnspan=2, pady=10)

submit = Button(frame, text='Submit', font=f2, width=10, fg='#F6FF73', bg='#203140',
state=NORMAL, command=palindrome, relief='raise')
submit.grid(row=0, column=1)

root.mainloop()