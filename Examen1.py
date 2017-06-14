from tkinter import*
from turtle import*
from math import*
import random
import time
#from twisted.internet import reactor

root = Tk()

root.config(bg = "red")#bg = "lavender"
root.geometry("640x480+280+200")#Tamaño ventada + Coordenadas de posicion X,Y
#root.maxsize(440, 320)#Permite dar un valor maximo a la ventana
#root.minsize(440, 320)#Permite dar un valor minimo a la ventana
root.title('EXAMEN - GEOVANNY DIAS')

def opcion1():#Figura Geometrica
    t = Pen()
    n = int(numinput("Figura Geometrica","Ingrese N lados: ","",3,5))
    g = 360/n
    t.reset()
    
    def dibujar(m):
        for j in range(0, n):
            t.forward(m)
            t.left(g)

    if n == 3:
        m = int(numinput("Medida","Ingrese medida del Triangulo: ","",0,200))
        dibujar(m)
        #Perimetro Triuangulo
        p=m*3
        #Area
        h=(sqrt(3)*m)/2
        area = (m*h)/2
        penup()
        hideturtle()
        goto(-50,-20)
        write("Su perimetro es: "+str(p),True)
        write(" ; Su area es: " + str(area))
        
    elif n == 4:
        m = int(numinput("Medida","Ingrese medida del Cuadrado: ","",0,200))
        dibujar(m)
        #Perimetro Cuadrado
        p=m*4
        #Area
        area = m**2
        penup()
        hideturtle()
        goto(-50,-20)
        write("Su perimetro es: "+str(p),True)
        write(" ; Su area es: " + str(area))
       
    elif n == 5:
        m = int(numinput("Medida","Ingrese medida de Pentagono: ","",0,200))
        dibujar(m)
        #Apoterma
        ap = (m)/(2*tan(180/n))
        #Perimetro Pentagono
        p=n*m
        #Area
        area = (p*ap)/2
        penup()
        hideturtle()
        goto(-50,-20)
        write("Su perimetro es: "+str(p),True)
        write(" ; Su area es: " + str(area))

    t.getscreen()._root.mainloop()

        

def opcion2():#Animacion
    
    class Ball:
        def __init__(self, canvas, color, posx, posy):
            self.canvas = canvas
            self.id = canvas.create_oval(10,10,25,25, fill=color)
            self.canvas.move(self.id, posx, posy)#posicion inicial

        def draw(self, dir1, dir2):
            self.canvas.move(self.id, dir1, dir2)

    tk = Tk()
    tk.title("Lluvia")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    def lluvia():
        pass
    
       
    ball = Ball(canvas, 'blue', 50, 100)
    ball1 = Ball(canvas, 'blue', 100, 100)
    ball2 = Ball(canvas, 'blue', 150, 100)
    ball3 = Ball(canvas, 'blue', 180, 100)
    ball4 = Ball(canvas, 'blue', 200, 100)
    ball5 = Ball(canvas, 'blue', 245, 100)
    n=0
    while 1:
        n=0
        while n <= 50:
            
            ball.draw(1,1)
            ball1.draw(1,1)
            ball2.draw(1,1)
            ball3.draw(1,1)
            ball4.draw(1,1)
            ball5.draw(1,1)
            
            tk.update_idletasks()
            tk.update()
            time.sleep(0.0001)
            n+=1
        n=0
    #reactor.callLater(3.5, lluvia, "hello, world")
    
        



Label(root, text="""Elija una opción:""", justify = LEFT,padx = 20).pack()

btn = Button(root, bd=10, text='Opción 1', width=10, command=lambda: opcion1()).pack()
btn = Button(root, bd=10, text='Opción 2', width=10, command=lambda: opcion2()).pack()


root.mainloop()
