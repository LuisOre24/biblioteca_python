from models.autor import Autor


class AutorController:
    def __init__(self):
        self.autor = Autor()

    def inicio(self):
        try:
            while True:
                print('==== AUTORES =====')
                print('''
                1.- Listar Autores
                2.- Buscar Autor
                3.- Registrar Autor
                4.- Actualizar Autor
                5.- Eliminar Autor
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
            autores = self.autor.get_autores()
            for autor in autores:
                print('***********************************')
                print(f'ID del Autor -> {autor[0]}')
                print(f'Nombres del Autor -> {autor[1]}')
                print(f'Apellidos del Autor -> {autor[2]}')
                print('***********************************')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')
    
    def buscar(self):
        try:
            id_autor = input('Ingrese el codigo del Autor -> ')
            where = {
                'id_autor' : id_autor
            }
            autor = self.autor.get_autor(where)
            print('***********************************')
            print(f'ID del Autor -> {autor[0]}')
            print(f'Nombres del Autor -> {autor[1]}')
            print(f'Apellidos del Autor -> {autor[2]}')
            print('***********************************')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def registrar(self):
        try:
            print('REGISTRO DE NUEVO AUTOR')
            nombres = input('ingrese el nombre del Autor -> ')
            apellidos = input('Ingrese los apellidos del Autor -> ')
            data = {
                'nombres' : nombres,
                'apellidos' : apellidos,
                'estado' : True
            }
            self.autor.insert_autor(data)
            print('AUTOR REGISTRADO CORRECTAMENTE')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def actualizar(self):
        try:
            print('ACTUALIZAR AUTOR')
            id_autor = int(input('Ingerse el ID del Autor a Actualizar -> '))
            nombres = input('ingrese el nombre del Autor -> ')
            apellidos = input('Ingrese los apellidos del Autor -> ')
            estado = input('Ingrese el estado del Autor (Disponible -> True / No Disponible -> False) -> ')
            where = {
                'id_autor' : id_autor
            }
            data = {
                'nombres' : nombres,
                'apellidos' : apellidos,
                'estado' : estado
            }
            self.autor.update_autor(where, data)
            print('AUTOR ACTUALIZADO CORRECTAMENTE')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def eliminar(self):
        try:
            print('ELIMINAR AUTOR')
            id_autor = input('Ingrese el ID del Autor a Eliminar ->')
            where = {
                'id_autor' : id_autor
            }
            self.autor.delete_autor(where)
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')
            


        