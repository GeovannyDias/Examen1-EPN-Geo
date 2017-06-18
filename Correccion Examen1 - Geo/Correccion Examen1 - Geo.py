#https://docs.python.org/2/library/turtle.html#turtle.fill
#24.5. turtle — Turtle graphics for Tk
from tkinter import *
from turtle import *
from math import *
import sys
import time
#=========================================================================================
                            #FUNCION FIGURA GEOMETRRICA
#=========================================================================================
def opcion1():  # Figura Geometrica
    try:
        #root.withdraw()
        t = Pen()
        setup(640,480, 200,50)
        title("Figura Geometrica - Geo")
        #screensize(640,480) #Lienzo
        n = int(numinput("Figura Geometrica", "Elija figura según su número de lados:\n"
                                              "\n3. Triángulo\n4. Cuadrado o Rectángulo"
                                              "\n5. Pentágono\n", "", 3, 5))
        g = 360 / n #Divide al Circulo en Grados

        def dibujar(m,altura,figura):#Dibuja Figura Geometrica  ========================
            for j in range(0, n):
                if  j==0:#Cambia Coordenada de Inicio
                    t.penup()
                    #t.hideturtle()
                    t.goto(-160,-150)
                    t.pendown()
                if n == 4 and figura == 2:# Slecciona figura cuadratica (Rectangulo)
                    xy=(j+1)%2
                    if xy !=0:#Base
                        t.forward(m)
                        t.left(g)
                    else:#Altura
                        t.forward(altura)
                        t.left(g)
                else:# Grafica el resto de figuras
                    t.forward(m)
                    t.left(g)

        if n == 3:#TRIANGULO  ===========================================================
            m = int(numinput("Longitud", "Ingrese Longitud:\nRango: (1-320)", "", 1, 320))
            root.state(newstate='withdraw')
            dibujar(m,0,0)
            p = m * 3#Perimetro
            h = (sqrt(3) * m) / 2#Area
            area = (m * h) / 2
            penup()
            hideturtle()
            goto(-160, -200)
            write("Perímetro = " + str(p))
            goto(-160, -220)
            write("Área = " + str(area))

        elif n == 4:#FIGURA CUADRADA  ===================================================

            figura=int(numinput("Figura", "1. Cuadrado => Lados Iguales"
                                       "\n2. Rectángulo => Base & Altura\n"
                                       "\nSeleccione Figura:\n(1-2)", "", 1, 2))
            if figura == 1:#Cuadrado  ***********************
                m = int(numinput("Longitud", "Ingrese Logitud:\nRango: (1-320)", "", 1, 320))
                root.state(newstate='withdraw')
                dibujar(m, 0, figura)
                p = m * 4#Perimetro Cuadrado
                area = m ** 2#Area
                penup()
                hideturtle()
                goto(-160, -200)
                write("Perímetro = " + str(p))
                goto(-160, -220)
                write("Área = " + str(area))
            else:#Rectangulo    ******************************
                m = int(numinput("Longitud", "Ingrese Base:\nRango: (1-320)", "", 1, 320))
                altura = int(numinput("Longitud", "Ingrese Altura:\nRango: (1-200)", "", 1, 200))
                root.state(newstate='withdraw')
                dibujar(m, altura, figura)
                p = (m + altura)*2# Perimetro Rectangulo
                area = m*altura# Area
                penup()
                hideturtle()
                goto(-160, -200)
                write("Perímetro = " + str(p))
                goto(-160, -220)
                write("Área = " + str(area))

        elif n == 5:#PENTAGONO  =========================================================
            m = int(numinput("Longitud", "Ingrese Longitud:\nRango: (1-250)", "", 1, 250))
            root.state(newstate='withdraw')
            dibujar(m,0,0)
            ap = (m) / (2 * tan(180 / n))#Apotema
            p = n * m#Perimetro
            area = (p * ap) / 2#Area
            penup()
            hideturtle()
            goto(-160, -200)
            write("Perímetro = " + str(p))
            goto(-160, -220)
            write("Área = " + str(area))

        root.destroy()
        t.getscreen()._root.mainloop()
        sys.exit("Termino La Ejecucion Exitosamente")
        # root.state(newstate='normal')
    except Exception:
        root.destroy()#Destruye lo procesos del ROOT
        print("Atencion Cancelo el Proceso")
        sys.exit("Termino La Ejecucion")

#=========================================================================================
                            #FUNCION ANIMACION (LLUVIA)
#=========================================================================================
def opcion2():  # Animacion
    try:
        global image
        root.state(newstate='withdraw')
        class Ball:

            def __init__(self, canvas, color, posx, posy):
                self.canvas = canvas
                self.id = canvas.create_oval(10, 8, 14, 18, fill=color)
                self.canvas.move(self.id, posx, posy)
                self.x = 3
                self.y = 7
                self.canvas_height = self.canvas.winfo_height()  # optiene la altura de canvas
                self.canvas_width = self.canvas.winfo_width()  # optiene el ancho de canvas

            def draw(self):
                self.canvas.move(self.id, self.x, self.y)
                #print("X: ", self.x, "   Y: ", self.y)
                pos = self.canvas.coords(self.id)
                #print(pos)
                if pos[1] <= 0:
                    #print("altura y = 2")
                    self.y = 7
                if pos[3] >= self.canvas_height:  # Al llegar al borde(Y) cambia a una posicion inicial
                    #print("Altura Final - Reset ", self.canvas_height)
                    self.y = -400
                if pos[0] <= 0:
                    #print("ancho x = 2")
                    self.x = 3
                if pos[2] >= self.canvas_width:  # Al llegar al borde(X) cambia a una posicion inicial
                    #print("Ancho Final - Reset ", self.canvas_width)
                    self.x = -500

        def dibujarBall():
            global ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10
            ball1 = Ball(canvas, 'blue', 5, 10)
            ball2 = Ball(canvas, 'Dodger Blue', 100, 30)
            ball3 = Ball(canvas, 'blue', 220, 20)
            ball4 = Ball(canvas, 'Dodger Blue', 340, 10)
            ball5 = Ball(canvas, 'blue', 450, 30)
            ball6 = Ball(canvas, 'Dodger Blue', 50, 150)
            ball7 = Ball(canvas, 'blue', 160, 190)
            ball8 = Ball(canvas, 'Dodger Blue', 380, 170)
            ball9 = Ball(canvas, 'blue', 300, 160)
            ball10 = Ball(canvas, 'Dodger Blue', 480, 180)

        def animacionDraw():
            ball1.draw()
            ball2.draw()
            ball3.draw()
            ball4.draw()
            ball5.draw()
            ball6.draw()
            ball7.draw()
            ball8.draw()
            ball9.draw()
            ball10.draw()

        tk = Toplevel()#Ventana secundaria
        tk.title("Lluvia - Geo")
        tk.resizable(0, 0)
        tk.wm_attributes("-topmost", 1)
        canvas = Canvas(tk, bg="lightblue", width=500, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        filename = PhotoImage(file="nube1.gif")# Carga imagen para asociar a canvas
        image = canvas.create_image(150, 50, anchor=W, image=filename)  # North, South, East, West
        tk.update()
        dibujarBall()

        while 1:
            animacionDraw()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.005)
        tk.mainloop()
        root.state(newstate='normal')
        #sys.exit("La Ejecucion Termino")
    except Exception:
        print("Atencion... La ventana animacion fue cerrada por el usuario.\nElija Otra Opcion")
        root.state(newstate='normal')

root = Tk()
root.config(bg="black")  # bg = "lavender"
root.geometry("640x480+280+200")  # Tamaño ventada + Coordenadas de posicion X,Y
root.resizable(0, 0)
root.title('EXAMEN - GEOVANNY DIAS')
# PANELES
# ==========================================================================================

frame = Frame(root, bd=4, width=640, height=480, relief="groove", bg="black")
frame.pack(fill=BOTH, padx=5, pady=5)  # side = BOTTOM

frameTop = Frame(frame, bd=4, relief="groove", bg="black")
frameTop.pack(fill=BOTH, padx=5, pady=5, ipadx=1, ipady=1, side=TOP)

frameBottom = Frame(frame, bd=4, relief="groove", bg="black")
frameBottom.pack(fill=BOTH, padx=5, pady=50, ipadx=1, ipady=150, side=BOTTOM)

Label(frameTop, text='Elija Una Opción:', justify=LEFT, padx=80, pady=10).pack()
btn = Button(frameBottom, bd=10, text='1. Figura Geométrica', width=25, command=lambda: opcion1()).pack()
btn = Button(frameBottom, bd=10, text='2. Animación Lluvia', width=25, command=lambda: opcion2()).pack()


root.mainloop()
