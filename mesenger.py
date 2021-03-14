from tkinter import *
import time
var = '0.2 (open file)'
name = 'Timur Timergaliev'
last_date = 0

def tools_window_f():
    tools_window = Toplevel()
    tools_window.title('tools')


def options_window_f():
    options_window = Toplevel()
    options_window.title('options')


def clear_history():
    text.config(state = NORMAL)
    text.delete(0.0, END)
    text.config(state = DISABLED)


def send_msg(event):
    global last_date
    text.config(state = NORMAL)

    # date = time.strftime(time.localtime())
    # t = time.strftime(time.localtime())
    date = ''
    t = ''

    if entry.get():
        msg = name + '\n'
        if last_date != date:
            msg += date + ' '
            last_date = date
        msg += t + ':\n' + entry.get() + '\n\n'
        text.insert(END, msg)
        text.config(state = DISABLED)
        entry.delete(0, END)

        save_history()


def save_history():
    t = open('history of messages.txt', 'w')
    data = text.get(0.0, END)
    t.write(data)


def load_saved_msgs():
    t = open('history of messages.txt', 'r')
    data = t.read()
    text.config(state = NORMAL)
    text.insert(END, data)
    text.config(state = DISABLED)


root = Tk()
root.geometry('275x400+200+200')
root.title('messenger ')

menu = Menu(root)
root.config(menu = menu)

filemenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'File', menu = filemenu)

filemenu.add_command(label = 'Очистка истории сообщений', command = clear_history)
filemenu.add_command(label = 'Выход', command = exit)
menu.add_command(label = 'Tools', command = tools_window_f)
menu.add_command(label = 'Options', command = options_window_f)

frame_text = Frame(root, )
frame_text.place(x = 5, y = 5, relwidth = 1, relheight = 1, width = -5, height = -30)
text = Text(frame_text)
text.place(x = 0, y = 0, relwidth = 1, relheight = 1, width = -55, height = 0)

btn1 = Button(frame_text, text = 1, width = 7, height = 3)
btn1.pack(anchor = NE, pady = 5)
btn2 = Button(frame_text, text = 2, width = 7, height = 3)
btn2.pack(anchor = NE, pady = 5)
btn3 = Button(frame_text, text = 3, width = 7, height = 3)
btn3.pack(anchor = NE, pady = 5)

frame_entry = Frame(root, )
frame_entry.pack(side = BOTTOM, fill = X)

entry = Entry(frame_entry)
entry.pack(side = LEFT, fill = X, expand = 1)

btn = Button(frame_entry, text = 'send', command = lambda: send_msg(0))
btn.pack(side = RIGHT, padx = 5)

entry.bind('<Return>', send_msg)

load_saved_msgs()

btn1.config(state = DISABLED)
btn2.config(state = DISABLED)
btn3.config(state = DISABLED)

root.mainloop()