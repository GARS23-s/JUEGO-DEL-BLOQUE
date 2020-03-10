from tkinter import*
ventana=Tk()
ventana.title("BLOQUES DE COLOR")
ventana.geometry("350x350")

global r,c
r=2
c=3

def mtx():
    global r,c

    for x in [1,2,3,4,5]:
        for y in [0,1,2,3,4]:

            A=Button(ventana, text=" ", bg="gray", height=2, width=4)
            A.grid(column=x, row=y)


    S=Button(ventana, text="S", bg="red", height=2, width=4)
    S.grid(column=c, row=r)

def izquierda():
    global c
    if (c==1):
        c=5
    else:
        c=c-1
    mtx()
    
def arriba():
    global r
    if (r==0):
        r=4
    else:
        r=r-1
    mtx()
    
def abajo():
    global r
    if (r==4):
        r=0
    else:
        r=r+1
    mtx()
    
def derecha():
    global c
    if (c==5):
        c=1
    else:
        c=c+1
    mtx()


Izq=Button(ventana, text="🢀", bg="green", height=2, width=4, command=izquierda)
Izq.grid(column=6, row=0)

Ar=Button(ventana, text="🢁", bg="orange", height=2, width=4, command=arriba)
Ar.grid(column=8, row=0)

Ab=Button(ventana, text="🢃", bg="yellow", height=2, width=4, command=abajo)
Ab.grid(column=7, row=0)

Der=Button(ventana, text="🢂", bg="brown", height=2, width=4, command=derecha)
Der.grid(column=9, row=0)
mtx()

ventana.mainloop()

