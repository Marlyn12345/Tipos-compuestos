def cargar():
    productos={}
    for x in range(5):
        nombre=input("Ingrese el nombre del producto：")
        precio=int(input("ingrese el precio："))
        productos[nombre]=precio
    return productos

def imprimir(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print (nombre, productos [nombre])


def imprimir_mayor100(productos):
    print("listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos [nombre]>100:
            print(nombre)

productos=cargar()
imprimir(productos)
imprimir_mayor100(productos)
