import os
generos = ["Ficcion", "No Ficcion", "Ciencia"]

inventario = []


ventas_realizadas = []

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def registrar_libro():
    limpiar_consola()
    print("--- Registrar Nuevo Libro ---")
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    genero = input("Ingrese el genero del libro (Ficcion, No Ficcion, Ciencia): ").capitalize()
    while genero not in generos:
        genero = input("Genero no valido. Ingrese el genero del libro nuevamente: ").capitalize()
    precio = float(input("Ingrese el precio del libro: "))
    
    
    if titulo.strip() == "" or autor.strip() == "" or genero.strip() == "" or precio <= 0:
        print("Error: Todos los campos son obligatorios y el precio debe ser mayor que cero.")
        return
    
    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "precio": precio
    }
    inventario.append(libro)
    print(f"Libro '{titulo}' registrado correctamente.")

def listar_libros():
    limpiar_consola()
    print("--- Listado de Libros en Inventario ---")
    if not inventario:
        print("No hay libros registrados.")
    else:
        for libro in inventario:
            print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Genero: {libro['genero']}, Precio: {libro['precio']}")

def registrar_venta():
    limpiar_consola()
    print("--- Registrar Venta ---")
    if not inventario:
        print("No hay libros registrados para vender.")
        return
    
    listar_libros()
    titulo = input("Ingrese el titulo del libro que desea vender: ")
    
    
    libro_encontrado = None
    for libro in inventario:
        if libro['titulo'] == titulo:
            print("titulo")