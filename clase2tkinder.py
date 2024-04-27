from tkinter import*

ventana=Tk()
ventana.title('CALCULADORA')
ventana.geometry('400x500')
#ventana.iconbitmap('thorfin.ico')
ventana.resizable(0,0)
ventana.config(bg='yellow',cursor='man')


boton1= Button(ventana,text='minimizar', command=ventana.iconify, bg='yellow')
boton1.pack()

def saludo():
    imprimir=Label(ventana, text='hola papus')
    imprimir.pack()
  

boton2= Button(ventana,text='Aceptar', command=saludo,bg='violet')
boton2.pack()







ventana.mainloop()