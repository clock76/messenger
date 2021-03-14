from tkinter import *

root = Tk()
root.title('mesenger 0.1')


def inserting(event):
    text.insert(END, entry.get())
    entry.delete(0, END)


text = Text()
text.pack()
entry = Entry(root)
entry.pack()


def pseudo_lambda():
    inserting(0)


btn = Button(text = 'button', command = pseudo_lambda)
btn.pack()

entry.bind('<Return>', inserting)

root.mainloop()