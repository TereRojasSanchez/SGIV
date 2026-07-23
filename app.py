from dao.proveedor_dao import ProveedorDAO
from models.proveedor import Proveedor

def ver_proveedores():
    try:
        proveedor_dao=ProveedorDAO()
        proveedores =proveedor_dao.obtener_todo()
        if len(proveedores)==0:
            print("No hay provedores registrados")
        else:
            for proveedor in proveedores:
                print(f"{proveedor.id} - {proveedor.nombre} -{proveedor.telefono}- {proveedor.correo}-{proveedor.producto} ")
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
                print("ERROR")
                print(e)
def insertar_proveedor():
    print("Insertar nuevo proveedor")
    nombre=input("Escriba el nombre del proveedor: ")
    telefono=int(input("Escriba el numero de contacto del proveedor: "))
    correo=input("Escriba el correo electronico: ")
    productoV=input("¿Que tipo de pruducto vende el proveedor? ")
    try:
        
        proveedor_dao=ProveedorDAO()
        ultimo_id=proveedor_dao.obtener_ultimo_id()+1
        proveedor=Proveedor(ultimo_id,nombre,telefono,correo,productoV)
        proveedor_dao.insertar(proveedor)
        print("La inserccion del nuevo proveedor fue exitosa")
    except Exception as e:
        print("Error al insertar el proveedor")    
        print(e)     

def actualizar_proveedor ():
    try:
        proveedor_dao=ProveedorDAO()
        print("Lista de proveedores ") 
        ver_proveedores()
        id=int(input("Selecciona el id del proveedor a actualizar: ")) 
        # 1. Buscamos los datos vigentes del usuario
        proveedor_actual=proveedor_dao.obtener_por_id(id)
        
        if proveedor_actual is None:
            print("El usuario no existe.")
            return

        print("1. Cambiar Nombre")
        print("2. Cambiar Telefono")
        print("3. Cambiar Correo")
        print("4. Cambiar producto")
        opcion=input("¿Qué atributo deseas modificar?: ")
    
        
        if opcion == "1":
            proveedor_actual.nombre=input(f"Nuevo nombre del proveedor: ")
        elif opcion == "2":
            proveedor_actual.telefono=int(input(f"Nueva Telefono: "))
        elif opcion == "3":
            proveedor_actual.correo=input(f"Nuevo correo : ")
        elif opcion == "4":
            proveedor_actual.producto=input(f"Nuevo producto : ")
        else:
            print("Opción no válida.")
            return
        
        proveedor_dao.actualizar(proveedor_actual)
        print("El proveedor fue actualizado con exito")
    except Exception as e:
        print("Error al actualizar el proveedor")
        print(e) 

def eliminar_proveedor ():
    try:
        proveedor_dao=ProveedorDAO()       
        print("Lista de los proveedores")
        ver_proveedores()
        id=int(input("Escribe el id del proveedor que quieres eliminar:"))
        proveedor_dao.eliminar(id)
        print(f"El proveedor numero {id} ha sido eliminado con exito")
    except Exception as e: 
        print(f"Error al eliminar el proveedor{id}")     
        print(e)


def main():
    print("Veterinaria Yolpaki ")
    print("1.Ver todos los Proveedores")   
    print("2.Insertar nuevo proveedor")
    print("3.Actualizar Proveedor")
    print("4.Eliminar proveedor")
    opcion=int(input("Selecciona una opcion (1-4):"))   

    match opcion:
        case 1:
            ver_proveedores()  
        case 2:    
            insertar_proveedor()  
        case 3:
            actualizar_proveedor()  
        case 4:
            eliminar_proveedor()    


if __name__=="__main__":
    main()                   