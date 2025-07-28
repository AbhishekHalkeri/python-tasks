################basic calculator########################
#STEP1: importing
from tkinter import *
#STEP2: gui interaction
window=Tk()
window.title('calculator')
window.geometry('500x500')
#STEP3: adding
#entry
E=Entry(window,width=25,borderwidth=5)
E.place(x=9,y=0)
#button
def click(num):
    result=E.get()
    E.delete(0,END)
    E.insert(0,str(result)+str(num))
b=Button(window,text='1',width=4,command=lambda:click(1))
b.place(x=10,y=30)
b=Button(window,text='2',width=4,command=lambda:click(2))
b.place(x=50,y=30)
b=Button(window,text='3',width=4,command=lambda:click(3))
b.place(x=90,y=30)
b=Button(window,text='4',width=4,command=lambda:click(4))
b.place(x=10,y=57)
b=Button(window,text='5',width=4,command=lambda:click(5))
b.place(x=50,y=57)
b=Button(window,text='6',width=4,command=lambda:click(6))
b.place(x=90,y=57)
b=Button(window,text='7',width=4,command=lambda:click(7))
b.place(x=10,y=84)
b=Button(window,text='8',width=4,command=lambda:click(8))
b.place(x=50,y=84)
b=Button(window,text='9',width=4,command=lambda:click(9))
b.place(x=90,y=84)
b=Button(window,text='0',width=4,command=lambda:click(0))
b.place(x=10,y=112)
b=Button(window,text='.',width=4)
b.place(x=50,y=112)
############operation buttons

#addition function
def add():
    n1=E.get()
    global math
    math='addition'
    global N1
    N1=int(n1)
    E.delete(0,END)
b=Button(window,text='+',width=4,command=add)
b.place(x=130,y=30)

#subtraction operation
def sub():
    n1=E.get()
    global math
    math='subtraction'
    global N1
    N1=int(n1)
    E.delete(0,END)
b=Button(window,text='-',width=4,command=sub)
b.place(x=130,y=57)


#multiplication operation
def mul():
    n1=E.get()
    global math
    math='multiplication'
    global N1
    N1=int(n1)
    E.delete(0,END)
p=Button(window,text='*',width=4,command=mul)
p.place(x=130,y=84)

#division operation
def div():
    n1=E.get()
    global math
    math='division'
    global N1
    N1=int(n1)
    E.delete(0,END)
m=Button(window,text='/',width=4,command=div)
m.place(x=90,y=112)


#equal to operation
def equal():
    n2=E.get()
    E.delete(0, END)
    if math=='addition':
        E.insert(0,N1+int(n2))
    elif math=='subtraction':
        E.insert(0,N1-int(n2))
    elif math=='multiplication':
        E.insert(0,N1*int(n2))
    elif math=='division':
        E.insert(0,N1/int(n2))
q=Button(window,text='=',width=4,command=equal)
q.place(x=130,y=112)

def clear():
    E.delete(0,END)
r=Button(window,text='Clear',width=21,command=clear)
r.place(x=10,y=140)


#STEP4: mainloop()
mainloop()
