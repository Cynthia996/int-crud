from tkinter import *
from tkinter import ttk, Frame
from tkinter import messagebox
import sqlite3

#-------------INTERFAZ GRAFICA------------------
root=Tk()
root.title("Menu Principal")
root.geometry("600x700")

#---------------MENU PRINCIPAL-----------------
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbdMenu=Menu(barraMenu, tearoff=0)
#bbdMenu.add_command(Label="Conectar")
#bbdMenu.add_command(Label="Salir")

barraMenu=Menu(barraMenu, tearoff=0)
#bbdMenu.add_command(Label="Borrar campos")

crudMenu=Menu(barraMenu,tearoff=0)
#crudMenu.add_command(Label="Crear")
#crudMenu.add_command(Label="Leerr")
#crudMenu.add_command(Label="Actualizar")
#crudMenu.add_command(Label="Borrar")
#crudMenu.add_command(Label="Ver todos")

ayudaMenu=Menu(barraMenu,tearoff=0)
#ayudaMenu.add_command(Label="Licencia")
#ayudaMenu.add_command(Label="Acerca de....")

#barraMenu.add_cascade(Label="BBDD",menu= bbddMenu)
#barraMenu.add_cascade(Label="Borrar",menu= borrarMenu)
#barraMenu.add_cascade(Label="CRUD",menu= crudMenuMenu)
#barraMenu.add_cascade(Label="Ayuda",menu= bbddMenu)


#---------------VENTANA PRODUCTOS-------------
#def Buscarproducto():
    #ventanaProductos = Toplevel(root)
    #ventanaProductos.title("Productos")
    #ventanaProductos.geometry("800x700")
    #ventanaProductos.resizable(0,0)
 
frame= Frame(root) 

cuadroID=Entry(frame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroProducto=Entry(frame)
cuadroProducto.grid(row=1, column=1, padx=10, pady=10)
cuadroPrecio=Entry(frame)
cuadroPrecio.grid(row=2, column=1, padx=10, pady=10)
cuadroProveedor=Entry(frame)
cuadroProveedor.grid(row=3, column=1, padx=10, pady=10)
cuadroStock=Entry(frame)
cuadroStock.grid(row=4, column=1, padx=10, pady=10)

idLabel=Label(frame, text="ID")
idLabel.grid(row=0, column=0, padx=10, pady=10)
proLabel=Label(frame, text="PRODUCTO")
proLabel.grid(row=1, column=0, padx=10, pady=10)
preLabel=Label(frame, text="PRECIO")
preLabel.grid(row=2, column=0, padx=10, pady=10)
provLabel=Label(frame, text="PROVEEDOR")
provLabel.grid(row=3, column=0, padx=10, pady=10)
stLabel=Label(frame, text="STOCK")
stLabel.grid(row=4, column=0, padx=10, pady=10)

frame1= Frame(root) 
frame1.place(x=50,y=290,width=600,height=300)                  
tabla=ttk.Treeview(frame1,columns=("col1","col2","col3","col4")) 

tabla.column("#0",width=50)  #!tabla proboducto
tabla.column("col1",width=80, anchor=CENTER)
tabla.column("col2",width=80, anchor=CENTER)
tabla.column("col3",width=80, anchor=CENTER)
tabla.column("col4",width=50, anchor=CENTER)
tabla.heading("#0",text="ID")
tabla.heading("col1",text="Producto", anchor=CENTER)
tabla.heading("col2",text="Precio", anchor=CENTER)
tabla.heading("col3",text="Proveedor", anchor=CENTER)
tabla.heading("col4",text="Stock", anchor=CENTER)

tabla.pack(side=LEFT,fill = Y)   #! barra de desplazamiento
sb = Scrollbar(frame1, orient=VERTICAL)
sb.pack(side=RIGHT, fill = Y)
tabla.config(yscrollcommand=sb.set)
sb.config(command=tabla.yview)

boton_productos = Button(frame, text="AGREGAR",bg="Violet",relief="flat",font=("Helvetica",10))
boton_productos.place(x=150, y=180)
boton_modificar_ventas = Button(frame, text="MODIFICAR",bg="Violet",relief="flat",font=("Helvetica",10))
boton_modificar_ventas.place(x=260,y=160)
boton_eliminar_ventas = Button(frame, text="ELIMINAR", bg="Violet",relief="flat",font=("Helvetica",10))
boton_eliminar_ventas.place(x=180,y=160)
boton_venta_buscar = Button(frame, text="BUSCAR", bg="Violet",relief="flat",font=("Helvetica",10))
boton_venta_buscar.place(x=40,y=200)
boton_venta_buscar_ = Entry(frame, bg="#E4E4E4",)
boton_venta_buscar_.place(x=120,y=200, width=200, height=25)
boton_listar = Button(frame, text="LISTAR", bg="Violet",relief="flat",font=("Helvetica",10))
boton_listar.place(x=120,y=160)
boton_agregar = Button(frame, text="AGREGAR",bg="Violet",relief="flat",font=("Helvetica",10))
boton_agregar.place(x=40,y=160)

boton_Ventas = Button(root, text="SALIR", bg="Violet",relief="flat", height=1, width=10,font=("Helvetica",10))
boton_Ventas.place(x=450,y=655)

     

#---------------VENTANA PRINCIPAL VENTAS--------------


botonbuscarpro= Button(root, text="BUSCAR ID",font=("Helvetica 12 bold"),compound = BOTTOM, height = 100, 
          width = 100,border="2",bg="white",).place(x=90,y=60)





root.mainloop