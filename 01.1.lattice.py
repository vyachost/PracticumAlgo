from tkinter import *

x0 = 0
x1 = 500
step = 20

root = Tk()

bFrame = Frame(root, width=x1, height=50)
c = Canvas(root, width=x1, height=x1, bd=0, borderwidth=0, relief=GROOVE)

def paintCross():
    for i in range(x0+1, x1+step, step):
        c.create_line(x0, i, x1, i, fill='blue', width=1)
    for i in range(x0, x1+step, step):
        c.create_line(i, x0, i, x1, fill='blue', width=1)

def paintRomb():
    for i in range(x0, x1+step, step):
        c.create_line(x0, i, i, x0, fill='blue', width=1)
        c.create_line(x0, i, x1-i, x1, fill='blue', width=1)
        c.create_line(x1, i, i, x1, fill='blue', width=1)
        c.create_line(x0+i, x0, x1, x1-i, fill='blue', width=1)

def paintAngle():
    for i in range(x0, x1+step, step):
        c.create_line(x0, x1, x0+i, x0, fill='blue', width=1)
        c.create_line(x0, x1, x1, x1-i, fill='blue', width=1)

def clearCanv():
    c.delete('all')

bCross = Button(bFrame, text='Cross', width=5, height=3, command=paintCross)
bRomb = Button(bFrame, text='Romb', width=5, height=3, command=paintRomb)
bAngle = Button(bFrame, text='Angle', width=5, height=3, command=paintAngle)
bClear = Button(bFrame, text='Clear', width=5, height=3, command=clearCanv)

bFrame.pack()
bCross.pack(side=LEFT)
bRomb.pack(side=LEFT)
bAngle.pack(side=LEFT)
bClear.pack(side=LEFT)
c.pack()

root.mainloop()