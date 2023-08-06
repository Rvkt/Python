from tkinter import *
from datetime import datetime
import pyperclip

root = Tk()
# root.geometry('500x500')
root.title('Create Directory')
root.configure(bg='#111C26')
root.attributes('-topmost', True)

now = datetime.now()
dt_str = now.strftime('%Y%m%d')
f = font=('Chathura ExtraBold', 20)



def date():
    global now;
    now = datetime.now()

    year_full = now.strftime('%Y')
    month_str = now.strftime('%b').upper()
    day_month = now.strftime('%d').zfill(2)
    day_name =  now.strftime('%a').upper()
    hour_24 =   now.strftime('%I').zfill(2)
    minutes =   now.strftime('%M').zfill(2)
    second =    now.strftime('%S').zfill(2)
    amPm =      now.strftime('%p').upper()

    clock_str = f'{year_full} {month_str} {day_month} {day_name} {hour_24} {minutes} {second}' 

    rtclock.config(text=clock_str)
    rtclock.after(500, date)

rtclock = Label(root, text='', fg='#f2b84b',bg='#111C26', font=('Chathura ExtraBold', 20))
rtclock.pack()

frame = Frame(root,)
frame.pack()

e = Entry(frame, width=50, font=('Chathura ExtraBold', 22))
e.grid(row=0, column=0)
e.get()

def sort_str():
    str = []
    global sorted_str
    
    for i in range(len(e.get())):
        if i % 2 == 0:
            str.append(e.get()[i].upper())
        else:
            str.append(e.get()[i].lower())
        sorted_str = ''.join(str)
    str_label.config(text=sorted_str)

def copy_str():
	pyperclip.copy(sorted_str)

submit_btn = Button(frame, text='submit', font=f, fg='#111c26', bg='#f2b84b', command=sort_str)
submit_btn.grid(row=0, column=1)

str_label = Label(frame, text='', width=50, height=2, font=f, bg='#D3D3D3')
str_label.grid(row=1, column=0)

copy_btn = Button(frame, text='Copy', font=f, fg='#111c26', bg='#f2b84b', command=copy_str)
copy_btn.grid(row=1, column=1)

date()
root.mainloop()