# Trabajo Colaborativo: "Mini Agenda de Contactos"
# Objetivo:
# Desarrollar una pequeña aplicación de consola en Python que funcione como una agenda de contactos. El objetivo es aplicar los conocimientos de programación estructurada (variables, constantes, tipos de datos, estructuras de control, funciones, etc.) y prácticas básicas de trabajo colaborativo con Git y GitHub.
# ________________________________________
# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.

import os
from functions import *

bandera_1=True
Usuarios = []
while bandera_1==True:
    os.system("cls")
    print("")
    print("###  Menu  ###")
    print("1.	Agregar un contacto: nombre, teléfono, email.")
    print("2.	Listar contactos: mostrar todos los contactos guardados.")
    print("3.	Buscar un contacto por nombre.")
    print("4.	Eliminar un contacto.")
    print("5.	Salir del programa.")
    print("")
    try:
        opcion_1=int(input("Ingrese una opcion: "))
         
        if opcion_1==1 :
            print("Hola")
            os.system("pause")
            
            
        elif opcion_1==2:
            print("Hola")
            os.system("pause")
            
            
        elif opcion_1==3:
            print("Hola")
            os.system("pause")
            
            
        elif opcion_1==4:
            print("Hola")
            os.system("pause")
            
            
        elif opcion_1==5:
            bandera_1=(salir())
            
        else:
            print("Opcion equivocada")
    
    except:
        print("Ingrese una opcion valida")
        os.system("pause")
 