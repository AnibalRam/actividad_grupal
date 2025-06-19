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
    