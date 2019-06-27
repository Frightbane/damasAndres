from Tkinter import *
ventana = Tk()
frame = Frame()
frame.pack()

def posin(event):
    info = event.widget.grid_info()
    f= info["row"]
    c= info["column"]
    print((info["row"], info["column"]))

def casillas(texto, colortexto, color, fila, columna):
    casilla = Button(frame, text = texto)
    casilla.grid(row = fila, column = columna)
    casilla.config(bg = color, fg = colortexto, width = 5)

    #
    casilla.bind("<Button 1>",posin)

def tablero():
    for f in range(2, 10):
        for c in range(2, 10):

            if((f%2 != 0) and (c%2 != 0)): 
                casillas(" ", 'black', 'black', f, c)
            elif((f%2 == 0) and (c%2 == 0)):
                casillas(" ", 'black', 'black', f, c)
            else:
                casillas(" ", 'white', 'white', f, c)
            

def clickNuevoJuego():
    for f in range(2, 10):
        for c in range(2, 10):
            if(f<5):
                if((f%2 != 0) and (c%2 != 0)):
                    casillas("x", 'red', 'black', f, c)
                elif((f%2 == 0) and (c%2 == 0)):
                    casillas("x", 'red','black', f, c)
            if(f>6):
                if((f%2 != 0) and (c%2 != 0)):
                    casillas("x", 'white', 'black', f, c)
                if((f%2 == 0) and (c%2 == 0)):
                    casillas("x", 'white', 'black', f, c)

tablero()

clickNuevoJuego()
ventana.mainloop()
