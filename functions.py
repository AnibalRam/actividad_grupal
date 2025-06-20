import os
def salir():
    os.system("cls")
    print("Cerrando programa")
    os.system("pause")
    return (False)

def agregar_contacto(Usuarios):
    os.system("cls")
    nombre= input("Nombre:")
    telefono= input("Telefono:")
    email= input("Email:")
    
    usuario =[nombre, telefono,email]
    os.system("pause")
    return(usuario)
print("contacto agregado\n")   

def mostrar_contacto(Usuarios):
    os.system("cls")
    for x in range (len(Usuarios)):
        print(f"{x}.{Usuarios[x]}")
        
    os.system("pause")    

def buscar_nombre(Usuarios):
    encontrado=0
    usuario = input("Ingrese nombre a buscar: ")
    for sub_usuario in Usuarios:
        if usuario in sub_usuario:
            print(f"Usuario encontrado:{sub_usuario}")
           
        else:
            encontrado=encontrado+1
       
        if encontrado==len(Usuarios):
            print("No hay usuarios con ese nombre")
    os.system("pause")


def eliminar_usuario(Usuarios):
   
    mostrar_contacto(Usuarios)
   
    eliminar=(input("Cual va a eliminar: "))
    for sub_usuario in Usuarios:
        if eliminar in sub_usuario:
            Usuarios.remove(sub_usuario)
            print(f"Usuario {eliminar} eliminado.")
            os.system("pause")


    mostrar_contacto(Usuarios)
   
