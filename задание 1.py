from tkinter import *
root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)
root.title('mesenger 0.1')
root.geometry('275x400')
root.resizable(width = False, height = True)


def history():
    hist = open('history of messages.txt', 'r')
    data = hist.read()
    text.insert(END, data)

def save_history():
    save = open('history of messages.txt', 'w')
    data = text.get(0.0, END)
    save.write(data)
    save.close()

def createnewwindow():
    createnewwindow = Toplevel(root)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="очистка")
filemenu.add_command(label="exit")


def inserting(event):
    text.config(state = NORMAL)
    text.insert(END, entry.get())
    entry.delete(0, END)
    text.config(state = DISABLED)
    save_history()


def cordfunc(event):
    print('x =', event.x, 'y =', event.y)


frm_text = Frame(root)
frm_text.pack()
frm_entry = Frame(root)
frm_entry.pack()
mainmenu.add_cascade(label='menu', menu = filemenu)
mainmenu.add_command(label='tools', command = createnewwindow)
mainmenu.add_command(label='options')

text = Text(frm_text)
text.pack()
entry = Entry(frm_entry)
entry.pack()


def func():
    inserting(0)

entry.bind('<Return>', inserting)


btn = Button(frm_entry, text='send', command=func)
btn.place()

root.bind('<Button-3>', cordfunc)

history()

text.config(state = DISABLED)

root.mainloop()
