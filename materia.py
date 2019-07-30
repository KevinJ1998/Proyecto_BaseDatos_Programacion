
from tkinter import ttk
from tkinter import *
import os
import pymysql
tk=Tk()
conn=pymysql.connect
conn=pymysql.connect(host='localhost',port=3306, user='root',passwd='',db='prueba')
cur=conn.cursor()

def notas():
    global notas_screen,codigo_est, codigo_entry
    codigo_est = StringVar()
    notas_screen = Toplevel(tk)
    notas_screen.title("CODIGO")
    notas_screen.geometry("200x200")
    Label(notas_screen,text = "Ingrese su codigo de estudiante:").pack()
    codigo_entry = Entry(notas_screen,textvariable = codigo_est)
    codigo_entry.pack()
    Button(notas_screen,text = "Acpetar",command = desplegar_notas).pack()

def desplegar_notas():
    global desplegar_notas_screen
    codigo_info = codigo_est.get()
    codigo_entry.delete(0, END)
    materia,nota = [],[]
    desplegar_notas_screen = Toplevel(tk)
    desplegar_notas_screen.title("NOTAS POR MATERIA")
    desplegar_notas_screen.geometry("200x200")
    Label(desplegar_notas_screen,text = "Materia con su nota").pack()
    seleccionar_materias = "SELECT nom_mat, nota FROM materia,est_mat WHERE est_mat.id_est like '"+codigo_info+"' and materia.id_mat like est_mat.id_mat"
    cur.execute(seleccionar_materias)
    resultados = cur.fetchall()
    for row in resultados:
        materia.append(str(row[0]))
        nota.append(str(row[1]))
    for i in range(len(materia)):
        Message(desplegar_notas_screen,text = (str(materia[i]+"\t"+nota[i]))).pack()
    

def menu():
    Label(tk,text="Seleccione una opcion", bg="red").pack()
    Button(tk,text = "Ver notas", command=notas).pack()
    Button(tk,text = "Cerrar Sesion",command =tk.quit).pack()
    tk.mainloop()
    
menu()
