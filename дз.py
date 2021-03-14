from tkinter import *
root = Tk()

lbl = Label()
lbl.pack()

txt = Text(height = 13, width = 32)
txt.place(x = 80, y = 5)

def func1(event):
    words = entry.get()
    print(words)
    txt.insert(END,words)
    entry.delete(0,END)


root.geometry('350x250')
btn = Button(text = '1', height = 3, width = 8, command = func1)
btn.place(x = 5, y = 5)
btn2 = Button(text = '2', height = 3, width = 8, command = func1)
btn2.place(x = 5, y = 65)
btn3 = Button(text = '3', height = 3, width = 8, command = func1)
btn3.place(x = 5, y = 125)
btn4 = Button(text = '4', height = 3, width = 8, command = func1)
btn4.place(x = 5, y = 185)
entry = Entry(width = 44)
entry.place(x = 80, y = 225)

root.title('задание 2.0(04.10.20)')

entry.bind('<Return>', func1)

root.mainloop()
print('программа завершена')


