from Clases.Estructuras import Producto
from Clases.Estructuras import Cliente
from Clases.Estructuras import Compra
from os import system

def registrarProducto(lista):
    codigo = input("Ingrese el codigo del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    desc = input ("Ingrese una descripcion clara del producto: ")
    precio = input("Ingrese el precio unitario del producto: ")
    NuevoProducto = Producto(codigo, nombre, desc, precio)
    lista.append(NuevoProducto)

def registrarCliente(lista):
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input ("Ingrese un correo electronico: ")
    nit = input("Ingrese el nit del cliente: ")
    NuevoCliente = Cliente(nombre, correo, nit)
    lista.append(NuevoCliente)

def buscarPorNit(listaCliente, nit):
    
    for cliente in listaCliente:
        if cliente.nit == nit:
            return True
        
    return False

def buscarPorCodigo(listaProducto, codigo, prod):
    for producto in listaProducto:
        if producto.codigo == codigo:
            prod = producto
            return True
        
    return False

def comprarProducto(listaProducto):
    system("cls")
    producto = Producto(codigo=None, nombre=None, desc= None, precio=None)
    codProducto = input("Ingrese el codigo de producto: ")
    if buscarPorCodigo(listaProducto, codProducto, producto):
        return producto
    else:
        print("Nit no registrado, vuelva a intentarlo!")
    return ""


def registrarCompra(listaCliente, listaProducto, listaCompra):
    while True:
        nit = input("Ingrese el nit del cliente: ")
        system("cls")
        if buscarPorNit(listaCliente, nit):
            break
        else:
            print("Nit no registrado, vuelva a intentarlo!")
            retry = int(input("¿Reintentar? (1: Si, 2: No):"))
            if retry == 1:
                continue
            else:
                return False

    sublistaProductos = []
    totalCompra = 0
    while True:
        print("------------- Menú Principal -------------")
        print("1. Agregar Producto")
        print("2. Terminar Compra (Genera Factura)")
        print("------------------------------------------")
        seleccion = obtenerOpcion(2)
        if seleccion == 1:
            producto = comprarProducto(listaProducto)
            if producto == "":
                print("Producto no existe, vuelva a intentarlo")
                continue
            
            totalCompra += producto.precio
            sublistaProductos.append(producto)

        elif seleccion == 2:
            id = len(listaCompra) + 1
            listaCompra.append(sublistaProductos, nit, id, totalCompra, totalCompra * 0.12)


    

def mostrarMenu():
    print("------------- Menú Principal -------------")
    print("1. Registrar Producto")
    print("2. Registrar Cliente")
    print("3. Realizar Compra")
    print("4. Reporte de Compra")
    print("5. Datos del Estudiante")
    print("6. Salir")
    print("------------------------------------------")

def obtenerOpcion(max):
    while True:
        try:
            opcion = int(input(f"Ingresa la opción deseada (1-{max}): "))
            if 1 <= opcion <= int(max):
                return opcion
            else:
                print("Opción inválida. Inténtalo nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejemplo de uso:



def main():
    listaProducto = []
    listaCliente = []
    listaCompras = []
    while True:
        mostrarMenu()
        seleccion = obtenerOpcion(6)
        if seleccion == 6:
            print("¡Hasta luego!")
            break
        elif seleccion == 1:
            registrarProducto(listaProducto)
        elif seleccion == 2:
            registrarCliente(listaCliente)
        elif seleccion == 3:
            registrarCompra(listaCliente, listaProducto, listaCompras)
            print("ss")
        system("cls")


if __name__ == "__main__":
    main()