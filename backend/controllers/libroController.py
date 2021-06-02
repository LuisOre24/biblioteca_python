from models.libro import Libro

class LibroController:
    def __init__(self):
        self.libro = Libro()

    def inicio(self):
        try:
            while True:
                print('==== LIBROS =====')
                print('''
        1.- Listar Libros
        2.- Buscar Libro
        3.- Registrar Libro
        4.- Actualizar Libro
        5.- Eliminar Libro
        6.- Salir
                ''')
                opcion = input('\n Ingrese una opcion -> ')
                if(opcion == '1'):
                    self.listar()
                elif(opcion == '2'):
                    self.buscar()
                elif(opcion == '3'):
                    self.registrar()
                elif(opcion == '4'):
                    self.actualizar()
                elif(opcion == '5'):
                    self.eliminar()
                elif (opcion == '6'):
                    break
                else:
                    print('Ingrese una opcion valida..')
            
        except Exception as ex:
            print(str(ex))

            
    def listar(self):
        try:
            libros = self.libro.get_libros()
            for libro in libros:
                print('***********************************')
                print(f'ID del Libro -> {libro[0]}')
                print(f'Nombre del Libro -> {libro[1]}')
                print(f'ID del Autor -> {libro[2]}')
                print(f'ID de la Editorial -> {libro[3]}')
                print(f'Año de Publicacion -> {libro[4]}')
                print(f'Categoria del Libro -> {libro[5]}')
                print(f'Estado -> {libro[6]}')
                print('***********************************')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def buscar(self):
        try:
            id_libro = input('Ingrese el codigo del Libro -> ')
            where = {
                'id_libro' : id_libro
            }
            libro = self.libro.get_libro(where)
            print('***********************************')
            print(f'ID del Libro -> {libro[0]}')
            print(f'Nombre del Libro -> {libro[1]}')
            print(f'ID del Autor -> {libro[2]}')
            print(f'ID de la Editorial -> {libro[3]}')
            print(f'Año de Publicacion -> {libro[4]}')
            print(f'Categoria del Libro -> {libro[5]}')
            print(f'Estado -> {libro[6]}')
            print('***********************************')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def registrar(self):
        try:
            print('REGISTRO DE NUEVO LIBRO')
            libro = input('Ingrese el nombre del Libro -> ')
            id_autor = input('ingrese al ID del Autor -> ')
            id_editorial = input('Ingrese el ID de la Editorial -> ')
            anio_publicacion = input('Ingrese el Año de Publicacion del Libro -> ')
            categoria = input('Ingrese la categoria del Libro -> ')
            data = {
                'nombreLibro' : libro,
                'id_autor' : id_autor,
                'id_editorial' : id_editorial,
                'anio_publicacion': anio_publicacion,
                'categoria' : categoria,
                'estado' : True
            }
            self.libro.insert_libro(data)
            print('LIBRO REGISTRADO CORRECTAMENTE')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def actualizar(self):
        try:
            print('ACTUALIZAR LIBRO')
            id_libro = input('Ingerse el ID del Libro a Actualizar -> ')
            libro = input('Ingrese el nombre del Libro -> ')
            id_autor = input('ingrese al ID del Autor -> ')
            id_editorial = input('Ingrese el ID de la Editorial -> ')
            anio_publicacion = input('Ingrese el Año de Publicacion del Libro -> ')
            categoria = input('Ingrese la categoria del Libro -> ')
            estado = input('Ingrese el estado del Libro (Disponible -> True / No Disponible -> False) -> ')
            where = {
                'id_libro' : id_libro
            }
            data = {
                'nombreLibro' : libro,
                'id_autor' : id_autor,
                'id_editorial' : id_editorial,
                'anio_publicacion': anio_publicacion,
                'categoria' : categoria,
                'estado' : estado
            }
            self.libro.update_libro(where, data)
            print('LIBRO ACTUALIZADO CORRECTAMENTE')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def eliminar(self):
        try:
            print('ELIMINAR LIBRO')
            id_libro = input('Ingrese el ID del Libro a Eliminar -> ')
            where = {
                'id_libro' : id_libro
            }
            self.libro.delete_libro(where)
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')
        