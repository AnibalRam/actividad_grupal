import os

def salir():
    os.system("cls")
    print("Cerrando programa")
    os.system("pause")
    return (False)

def agregar_contacto(Usuarios):
    os.system("cls")
    print("")
    print("### Registrando usuarios ###")
    print("")
    #usuario =[nombre,telefono,email]

    nombre=""
    while len(nombre)<3:
        nombre= input("Nombre:").title()

    for usuario in Usuarios:
        if usuario[0].title() == nombre.title():
            print(f"Usuario {usuario[0]} ya existe")
            print("Volviendo al menu")
            os.system("pause")
            return None

    print("")
    
    telefono=0
    while telefono==0:
        try:
            telefono_verificar= int(input("Telefono:"))
            if (telefono_verificar)> 900000000 and (telefono_verificar)<=999999999:
                telefono=telefono_verificar
            elif (telefono_verificar)< 900000000 or (telefono_verificar)>999999999:
                print("El telefono debe tener 9 numeros y partir con un 9. ")
            
            
        except:
            print("Formato equivocado, solo 9 numeros")
    print("")

    email_validar=False
    while email_validar==False:
        email= input("Email:")
        if len(email)>10 and email.endswith("@gmail.com"):
            email_validar=True
        else:
            print("El correo debe ser un correo de extension @gmail.com")

    print("")
    
    usuario =[nombre,telefono,email]
    print("contacto agregado\n")   
    os.system("pause")

    return(usuario)


def mostrar_contacto(Usuarios):
    os.system("cls")
    print("### Mostrando usuarios registrados: ###")
    print("")

    if len(Usuarios)==0:
        print("No hay usuarios registrados")
    else:
        for x in range (len(Usuarios)):
            print(f"{x+1}.{Usuarios[x]}")

    print("")   
    os.system("pause")    

def buscar_nombre(Usuarios):

    os.system("cls")
    print("")
    print("### Buscando usuarios por nombre ###")
    print("")
    if len(Usuarios)==0:
        print("No hay usuarios registrados")
        print("")
    else:
        encontrado=0
        usuario = input("Ingrese nombre a buscar: ").title()
        for sub_usuario in Usuarios:
            if usuario in sub_usuario:
                print(f"Usuario encontrado:{sub_usuario}")
                
            else:
                encontrado=encontrado+1
            
            if encontrado==len(Usuarios):
                print("No hay usuarios con ese nombre")
    os.system("pause")

def eliminar_usuario(Usuarios):
    if len(Usuarios)==0:
        os.system("cls")
        print("No hay usuarios registrados")
        os.system("pause")
    else:
        mostrar_contacto(Usuarios)

        print("")
        print("### Eliminando Usuarios ###")
        print("")
    
        eliminar=(input("¿Cual va a eliminar?: ")).title()
        print("")

        eliminado = False

        for sub_usuario in Usuarios:
            if eliminar == sub_usuario[0]:
                Usuarios.remove(sub_usuario)
                print(f"Usuario {eliminar} eliminado.")
                eliminado = True
                os.system("pause")
                mostrar_contacto(Usuarios)
        
        if not eliminado:
            print("No se encontró ningún usuario con ese nombre.")
            os.system("pause")
