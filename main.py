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

def buscarPorNit(listaCliente, nit, cli):
    
    for cliente in listaCliente:
        if cliente.nit == nit:
            cli = cliente
            return True
        
    return False

def buscarPorCodigo(listaProducto, codigo, prod):
    for producto in listaProducto:
        if producto.codigo == codigo:
            prod = producto
            return True
        
    return False

def buscarProducto(ListaProducto, codigo):
    for producto in ListaProducto:
        if producto.codigo == codigo:
            return producto
    return False

def buscarCliente(ListaCliente, nit):
    for cliente in ListaCliente:
        if cliente.nit == nit:
            return cliente
    return False

def comprarProducto(listaProducto):
    system("cls")
    codProducto = input("Ingrese el codigo de producto: ")
    producto = buscarProducto(listaProducto, codProducto)
    if producto is not None:
        return producto
    else:
        print("Producto no registrado, vuelva a intentarlo!")
    return ""


def registrarCompra(listaCliente, listaProducto, listaCompra):
    while True:
        nit = input("Ingrese el nit del cliente: ")
        cliente = Cliente(nombre=None, correo=None, nit=None)
        system("cls")
        if buscarPorNit(listaCliente, nit, cliente):
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
            
            totalCompra += int(producto.precio)
            sublistaProductos.append(producto)

        elif seleccion == 2:
            id = len(listaCompra) + 1
            compra = Compra(sublistaProductos, nit, id, totalCompra, totalCompra * 0.12)
            listaCompra.append(compra)
            return True

def reporteCompra(listaCompra, listaCliente):
    cliente = Cliente(nombre=None, correo=None, nit=None)
    system("cls")
    idCompra = input("Ingrese el ID de compra: ")
    flgExiste = False
    for compra in listaCompra:
        if int(compra.id) != int(idCompra):
            continue

        print("\n")
        print(f"------------ REPORTE DE COMPRA {compra.id} ------------")
        print("CLIENTE: ")
        cliente = buscarCliente(listaCliente, compra.cliente)
        print(f"     Nombre:    {cliente.nombre}")
        print(f"     Correo:    {cliente.correo}")
        print(f"     Nit:       {cliente.nit}")
        print("\n\n")
        print("ARTICULOS COMPRADOS")
        for producto in compra.lista:
            print(f"     {producto.nombre}  |  Q {float(producto.precio)}")
        print("\n\n")
        print(f"Total: Q {float(compra.total)}")
        print(f"Impuesto: Q {float(compra.total)}")
        print("---------------------------------------------------")
        flgExiste = True
        break

    if not flgExiste:
        print(f"No existe compra con ID {idCompra} asignado.")

    input()

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
        elif seleccion == 4:
            reporteCompra(listaCompras, listaCliente)
        elif seleccion == 5:
            system("cls")
            print("--------------------------------------------------")
            print("NOMBRE: CRISTIAN GIOVANNI ESTRADA RAMIREZ")
            print("CARNET: 202006413")
            print("--------------------------------------------------")
            input()
        system("cls")


if __name__ == "__main__":
    main()