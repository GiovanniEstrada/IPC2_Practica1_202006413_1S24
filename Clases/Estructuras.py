class Producto:

    def __init__(self, codigo, nombre, desc, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.desc = desc
        self.precio = precio

class Cliente:

    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

class Compra:

    def __init__(self, lista, cliente, id, total, iva):
        self.lista = lista
        self.cliente = cliente
        self.id = id
        self.total = total
        self.iva = iva