#importar modulos
from tkinter import messagebox
import pymysql
from tkinter import *
import os
#conexion con la base de datos 
conn=pymysql.connect(host='localhost',port=3306, user='root',passwd='',db='prueba')
cur = conn.cursor()

# Ventana de registro
def register_prof():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Registro")
    register_screen.geometry("300x250")
 
    global username_prof
    global password_prof
    global username_entry_prof
    global password_entry_prof
    username_prof = StringVar()
    password_prof = StringVar()
 
    Label(register_screen, text="Por favor ingrese los datos abajo", bg="red").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Usuario * ")
    username_lable.pack()
    username_entry_prof = Entry(register_screen, textvariable=username_prof)
    username_entry_prof.pack()
    password_lable = Label(register_screen, text="Contraseña * ")
    password_lable.pack()
    password_entry_prof = Entry(register_screen, textvariable=password_prof, show='*')
    password_entry_prof.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Registro", width=10, height=1, bg="red", command = register_user_prof).pack()
 
def register_est():
    global register_screen1
    register_screen1 = Toplevel(main_screen)
    register_screen1.title("Registro")
    register_screen1.geometry("300x250")
 
    global username_est
    global password_est
    global username_entry_est
    global password_entry_est
    username_est = StringVar()
    password_est = StringVar()
 
    Label(register_screen1, text="Por favor ingrese los datos abajo", bg="red").pack()
    Label(register_screen1, text="").pack()
    username_lable = Label(register_screen1, text="Usuario * ")
    username_lable.pack()
    username_entry_est = Entry(register_screen1, textvariable=username_est)
    username_entry_est.pack()
    password_lable = Label(register_screen1, text="Contraseña * ")
    password_lable.pack()
    password_entry_est = Entry(register_screen1, textvariable=password_est, show='*')
    password_entry_est.pack()
    Label(register_screen1, text="").pack()
    Button(register_screen1, text="Registro", width=10, height=1, bg="red", command = register_user_est).pack()
 
# Ventana para iniciar sesion
 
def login_profesor():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Iniciar Sesión")
    login_screen.geometry("300x250")
    Label(login_screen, text="Por favor ingrese los datos para acceder").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Usuario * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Contraseña * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Iniciar Sesión", width=10, height=1, command = login_verify_profesor).pack()

def login_estudiante():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Iniciar Sesión")
    login_screen.geometry("300x250")
    Label(login_screen, text="Por favor ingrese los datos para acceder").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Usuario * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Contraseña * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Iniciar Sesión", width=10, height=1, command = login_verify_estudiante).pack()

#la siguiente funcion muestra botones para ingresar sesion dependiendo del usuario
def login2():
    global login_screen2
    login_screen2 = Toplevel(main_screen)
    login_screen2.title("Seleccione una opción")
    Button(login_screen2, text = "PROFESOR", command=login_profesor).pack()
    Button(login_screen2, text = "ESTUDIANTE", command=login_estudiante).pack()

 
# Evento en el boton registrar
 
def register_user_est():
    # aqui se ingesara al usuario estudiante en la tabla estudiante y en la tabla cuenta que seria de los estudiantes
    username_info = username_est.get()
    password_info = password_est.get()
    
    registrar_bd = "INSERT INTO estudiante(id_est,nom_est) VALUES (NULL,'"+username_info+"')"
    cur.execute(registrar_bd)
    conn.commit()
    registrar_cuenta = "INSERT INTO cuenta(passwd_cuenta,nombre_usuario,id_usuario) VALUES ('"+password_info+"','"+username_info+"',NULL)"
    #el id del usuario se manda como null ya se es PRIMARY KEY en la base de datos de incremento, por lo que se pone por defecto un numero
    cur.execute(registrar_cuenta)
    conn.commit()

    # se almacena los datos en un archivo como respaldo
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry_est.delete(0, END)
    password_entry_est.delete(0, END)
 
    Label(register_screen1, text="Registro Exitoso", fg="green", font=("calibri", 11)).pack()
 
def register_user_prof():
    # en esta funcion se va ingresar al usuario profesor en la tabla profesor y en la tabla cuenta_prof 
    username_info = username_prof.get()
    password_info = password_prof.get()
    registrar_bd = "INSERT INTO profesor(id_prof,nom_prof) VALUES (NULL,'"+username_info+"')"
    cur.execute(registrar_bd)
    conn.commit()
    registrar_cuenta_prof = "INSERT INTO cuenta_prof(id_usuario_prof,nombre_cuenta_prof,passwd_cuenta_prof) VALUES (NULL,'"+username_info+"','"+password_info+"')"
    cur.execute(registrar_cuenta_prof)
    conn.commit()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry_prof.delete(0, END)
    password_entry_prof.delete(0, END)
 
    Label(register_screen, text="Registro Exitoso", fg="green", font=("calibri", 11)).pack()


def registro():
    global register_screen2
    register_screen2 = Toplevel(main_screen)
    register_screen2.title("Seleccione una opcion")
    Button(register_screen2, text = "PROFESOR", command=register_prof).pack()
    Button(register_screen2, text = "ESTUDIANTE", command=register_est).pack()


# Evento en el boton iniciar sesion
def login_verify_profesor():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    lis_aux,lis_aux1 = [],[] #listas auxiliares para poder reconocer los elementos del sql
    buscar_profesor = "SELECT nombre_cuenta_prof FROM cuenta_prof"
    cur.execute(buscar_profesor)
    lista_profesores = cur.fetchall()# almacenar todos los elementos en una lista
    for row in lista_profesores:
        lis_aux.append(str(row[0]))
    if username1 in lis_aux:
        verificar_contrsena = "SELECT passwd_cuenta_prof FROM cuenta_prof"
        cur.execute(verificar_contrsena)
        contrasenias = cur.fetchall()
        for row1 in contrasenias:
            lis_aux1.append(row1[0])
        if password1 in lis_aux1:
            login_sucess_profesor()
 
        else:
            password_not_recognised()
    else:
        user_not_found()


def login_verify_estudiante():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    lis_aux,lis_aux1 = [],[]
    buscar_estudiante = "SELECT nombre_usuario FROM cuenta"
    cur.execute(buscar_estudiante)
    lista_estudiante = cur.fetchall() #almacena todos los elementos de la base de datos en una lista
    for row in lista_estudiante:
        lis_aux.append(str(row[0]))

    if username1 in lis_aux:
        verificar_contrsena = "SELECT passwd_cuenta FROM cuenta" # mandar otro comando para las contraseñas
        cur.execute(verificar_contrsena)
        contrasenias = cur.fetchall()
        for row1 in contrasenias:
            lis_aux1.append(str(row1[0])) 
            if password1 in lis_aux1:
                login_sucess_estudiante()
 
            else:
                password_not_recognised()
 
    else:
        user_not_found()
 

 
def menu_profesor():
    os.system("bd.py")

#Comprobar si el usuario existe
def login_sucess_profesor():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Exito")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Entrada Exitosa").pack()
    Button(login_success_screen, text="OK", command=menu_profesor).pack()

def menu_estudiante():
    os.system("materia.py")
    
def login_sucess_estudiante():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Exito")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Entrada Exitosa").pack()
    Button(login_success_screen, text="OK", command=menu_estudiante).pack()

# Contraseña incorrecta
 
def password_not_recognised():
    messagebox.showinfo("Alerta","Contraseña Incorrecta")
 
# Usuario no encontrado
 
def user_not_found():
    messagebox.showinfo("Alerta","Usuario no encontrado")
  
# Ventana Principal
 

def main():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Ingreso a la cuenta")
    Label(text="Elija una opción", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Iniciar Sesión", height="2", width="30", command = login2).pack()
    Label(text="").pack()
    Button(text="Registro", height="2", width="30", command=registro).pack()
 
    main_screen.mainloop()
 
 
main()
