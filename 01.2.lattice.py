from tkinter import *

x0, x1 = 0, 500
y0, y1 = 0, 500
step = 20

root = Tk()

bFrame = Frame(root, width=x1, height=50)
c = Canvas(root, width=x1, height=y1, bd=0, borderwidth=2, relief=GROOVE)

def clearCanv():
    c.delete('all')

def drawCanv():
    for i in range(x0+4, x1, step*2):
        for j in range(y0+4, y1, step*2):
            c.create_rectangle(i, j, i+step, j+step, fill='green')

bDraw = Button(bFrame, text='Draw', width=5, height=3, command=drawCanv)
bClear = Button(bFrame, text='Clear', width=5, height=3, command=clearCanv)


bFrame.pack()
bDraw.pack(side=LEFT)
bClear.pack(side=LEFT)
c.pack()

root.mainloop()