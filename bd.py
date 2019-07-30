from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import os
import pymysql
tk=Tk()
conn=pymysql.connect(host='localhost',port=3306, user='root',passwd='',db='prueba')
cur=conn.cursor()
    
def ingresar():
    global ingresar_datos, nombre_est,apellido_est,nombre,apellido
    nombre_est = StringVar()
    apellido_est = StringVar()
    ingresar_datos = Toplevel(tk)
    ingresar_datos.title("Ingreso de datos")
    ingresar_datos.geometry("300x250")
    Label(ingresar_datos,text = "Ingrese el nombre del estudiante: ").pack()
    nombre = Entry(ingresar_datos, textvariable = nombre_est)
    nombre.pack()
    Label(ingresar_datos,text = "Ingrese el apellido del estudiante: ").pack()
    apellido = Entry(ingresar_datos,textvariable = apellido_est)
    apellido.pack()
    Button(ingresar_datos,text = "Aceptar",command = aceptar).pack()

def aceptar():
    #se registrara al estudiante con nombre y apellido para le curso
    info_nombre = nombre_est.get()
    info_apellido = apellido_est.get()
    sql="INSERT INTO  estudiante (id_est,nom_est,apel_est) VALUES (NULL,'"+info_nombre+"','"+info_apellido+"')"
    nombre.delete(0, END)
    apellido.delete(0, END)
    cur.execute(sql)
    Label(ingresar_datos,text = "Registro añadido").pack()
    conn.commit()
    
def ingresar_notas():
    global ingresar_notas_screen, materias,cod_est,nota_est,codigo,nota
    cod_est = StringVar()
    nota_est = StringVar()
    ingresar_notas_screen = Toplevel(tk)
    ingresar_notas_screen.title("Ingreso de datos")
    ingresar_notas_screen.geometry("300x250")
    Label(ingresar_notas_screen,text = "Escoja la materia: ").pack()
    materias = ttk.Combobox(ingresar_notas_screen,state = "readonly")
    materias.pack()
    cur.execute("SELECT nom_mat from materia")
    lista_materias = cur.fetchall() # la funcion fetchall devuelve todos los elementos como una tupla
    materias["values"] = lista_materias #se llena todo el combo box con los nombres de las materias de la tabla materia
    Label(ingresar_notas_screen,text = "Ingrese el codigo del estudiante:").pack()
    codigo = Entry(ingresar_notas_screen,textvariable = cod_est) #para poder ingresar la nota se necesita el codigo del estudiante
    codigo.pack()
    Label(ingresar_notas_screen,text = "Ingrese la nota:").pack()
    nota = Entry(ingresar_notas_screen,textvariable = nota_est)
    nota.pack()
    Button(ingresar_notas_screen,text = "Aceptar",command = aceptar_notas).place(x = 100, y = 160)
    Label(ingresar_notas_screen,text = "Ver los codigos de los estudiantes").place(x = 10, y = 200)
    Button(ingresar_notas_screen,text = "Aqui",command = ver_codigos).place(x = 100, y = 220) 
    #este boton es en caso de que no recuerde el codigo del estudinate


def aceptar_notas():
    info_codigo = cod_est.get()
    info_nota = nota_est.get()
    indice = materias.current() #el indice me toma la posicion en la que esta ubicado el combobox pero se debe recordar que empiez en 0
    insertar = "INSERT INTO est_mat VALUES ('"+str(indice+1)+"','"+info_codigo+"','"+info_nota+"')"
    codigo.delete(0, END)
    nota.delete(0, END)
    cur.execute(insertar)
    Label(ingresar_notas_screen,text = "Nota registrada").pack()
    conn.commit()

def ver_codigos(): # muestra todos los cosigos de los estudiantes con su respectivo estudiante
    global frame_codigos
    frame_codigos = Toplevel(tk)
    frame_codigos.title("Codigos de los estudiantes")
    frame_codigos.geometry("200x200")
    buscar_codigos = "SELECT id_est,nom_est FROM estudiante"
    cur.execute(buscar_codigos)
    codigos = cur.fetchall()
    Message(frame_codigos,text = str(codigos)).pack()

def eliminar():
    global eliminar_screen,cod,id_estd
    id_estd = StringVar()
    eliminar_screen = Toplevel(tk)
    eliminar_screen.title("Eliminar un registro")
    eliminar_screen.geometry("200x200")
    Label(eliminar_screen,text = "Ingrese el codigo de estudiante que desea eliminar:").pack()
    cod = Entry(eliminar_screen,textvariable = id_estd) #se elimina al los estudiante por su codigo
    cod.pack()
    Button(eliminar_screen,text = "Eliminar",command = eliminar_registro).pack()

def eliminar_registro():
    info_cod = id_estd.get()
    sql="DELETE from  estudiante where id_est like '"+info_cod+"'"
    Label(eliminar_screen,text = "registro eliminado").pack()
    cur.execute(sql)
    cod.delete(0, END)
    conn.commit()


def modificar(): # en esta funcion solo se modificara las notas no los datos en si del estudiante
    global modificar_screen, estudiantes_mod, materias_mod, nota_mod,nota_mod_entry
    nota_mod = StringVar()
    nota_actual = StringVar()
    modificar_screen = Toplevel(tk)
    modificar_screen.title("Modificar datos")
    modificar_screen.geometry("300x250")
    materias_mod = ttk.Combobox(modificar_screen, state = "readonly")
    materias_mod.pack()
    cur.execute("SELECT nom_mat FROM materia")
    lista_materias_mod = cur.fetchall()
    materias_mod["values"] = lista_materias_mod
    estudiantes_mod = ttk.Combobox(modificar_screen, state = "readonly")
    estudiantes_mod.pack()
    cur.execute("SELECT nom_est FROM estudiante")
    lista_estudiantes_mod = cur.fetchall()
    estudiantes_mod["values"] = lista_estudiantes_mod
    Label(modificar_screen, text = "Nota a cambiar:").pack()
    nota_mod_entry = Entry(modificar_screen, textvariable = nota_mod)
    nota_mod_entry.pack()
    Button(modificar_screen,text = "Ver notas",command = ver_notas).pack() # boton para ver las notas actuales que se quieren cambiar
    Button(modificar_screen, text = "Modificar", command = modificar_nota).pack()

def ver_notas():
    global frame_notas
    notas_estudiante = "SELECT nom_est,apel_est,nom_mat,nota FROM estudiante,materia,est_mat WHERE estudiante.id_est like est_mat.id_est and materia.id_mat like est_mat.id_mat"
    frame_notas = Toplevel(tk)
    frame_notas.title("NOTAS")
    frame_notas.geometry("350x200")
    cur.execute(notas_estudiante)
    notas_est = cur.fetchall()
    Message(frame_notas, text = str(notas_est)).pack()

def modificar_nota():
    info_nota_mod = nota_mod.get()
    indice_est = estudiantes_mod.current() 
    """"Como se uso combo box se deben registrar los indices en los que se ecuentra para poder mandar 
    como un comando sql"""
    indice_mat = materias_mod.current()
    mod="UPDATE est_mat set nota='"+info_nota_mod+"' WHERE id_est like '"+str(indice_est+1)+"' AND id_mat like '"+str(indice_mat+1)+"'"
    Label(modificar_screen,text = "registro actualizado").pack()
    nota_mod_entry.delete(0, END)
    cur.execute(mod)
    conn.commit()

#nota mas alta para cada materia
def nota_mas_alta():
    global nota_alta_screen
    nota_alta_screen = Toplevel(tk)
    nota_alta_screen.title("Nota alta por materia")
    nota_alta_screen.geometry("300x250")
    sql="SELECT est_mat.id_mat,nom_mat, max(nota) from est_mat,materia WHERE materia.id_mat like est_mat.id_mat GROUP BY est_mat.id_mat"
    cur.execute(sql)
    nota_alta = cur.fetchall()
    Message(nota_alta_screen,text = str(nota_alta)).pack()

    
#nota mas baja para cada materia
def nota_mas_baja():
    global nota_baja_screen
    nota_baja_screen = Toplevel(tk)
    nota_baja_screen.title("Nota baja por materia")
    nota_baja_screen.geometry("350x200")
    sql="SELECT est_mat.id_mat,nom_mat, min(nota) from est_mat,materia WHERE materia.id_mat like est_mat.id_mat GROUP BY est_mat.id_mat"
    cur.execute(sql)
    nota_baja = cur.fetchall()
    Message(nota_baja_screen,text = str(nota_baja)).pack()
    
#promedio de nota para cada materia
def promedio():
    global promedio_screen
    promedio_screen = Toplevel(tk)
    promedio_screen.title("Promedio por materia")
    promedio_screen.geometry("350x200")
    sql="SELECT est_mat.id_mat,nom_mat, avg(nota) from est_mat,materia WHERE materia.id_mat like est_mat.id_mat GROUP BY est_mat.id_mat"
    cur.execute(sql)
    promedio_materia = cur.fetchall()
    Message(promedio_screen,text = str(promedio_materia)).pack()

#notas totales    
def cantidad_de_notas():
    sql="SELECT count(*) from est_mat"
    cur.execute(sql)
    total_notas = cur.fetchall()
    messagebox.showinfo("Cantidad de notas totales",str(total_notas))
    

#promedio por un estudiante ingresado
def promedio2():
    global promedio_est_screen,nombres_est,promedio_est
    promedio_est = StringVar()
    promedio_est_screen = Toplevel(tk)
    promedio_est_screen.title("Promedio de cada estudiante")
    promedio_est_screen.geometry("350x200")
    Label(promedio_est_screen,text = "Elija el nombre del estudiante:").pack()
    nombres_est = ttk.Combobox(promedio_est_screen,state = "readonly")
    nombres_est.pack()
    cur.execute("SELECT nom_est FROM estudiante")
    lista_estudiantes = cur.fetchall()
    nombres_est["values"] = lista_estudiantes
    Label(promedio_est_screen,textvariable = promedio_est).pack()
    Button(promedio_est_screen,text = "Ver promedio",command = ver_promedio).pack()

def ver_promedio():
    indice_nom_est = nombres_est.current()
    sql="SELECT avg(nota) from est_mat,estudiante where est_mat.id_est like '"+str(indice_nom_est+1)+"'"
    cur.execute(sql) 
    resultado = cur.fetchall()
    promedio_est.set(str(resultado))
    

def menu():
    Label(tk,text="Seleccione una opcion", bg="red").pack()
    Button(tk,text = "Ingresar estudiante", command= ingresar).pack()
    Button(tk,text = "Ingresar notas",command = ingresar_notas).pack()
    Button(tk,text = "Eliminar datos", command=eliminar).pack()
    Button(tk,text = "Modificar datos", command=modificar).pack()
    Button(tk,text = "Cantidad de notas", command=cantidad_de_notas).pack()
    Button(tk,text = "Notas mas alta", command=nota_mas_alta).pack()
    Button(tk,text = "Notas mas baja", command=nota_mas_baja).pack()
    Button(tk,text = "Promedio", command=promedio).pack()
    Button(tk,text = "Promedio para el estudiante", command=promedio2).pack()
    Button(tk,text = "Salir",command = tk.quit).pack()
    
    tk.mainloop()
    
menu()
