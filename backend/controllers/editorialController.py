from re import escape
from models.editorial import Editorial

class EditorialController:
    def __init__(self):
        self.editorial = Editorial()

    def inicio(self):
        try:
            while True:
                print('==== EDITORIALES =====')
                print('''
                1.- Listar Editoriales
                2.- Buscar Editorial
                3.- Registrar Editorial
                4.- Actualizar Editorial
                5.- Eliminar Editorial
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
            editoriales = self.editorial.get_editoriales()
            for editorial in editoriales:
                print('***********************************')
                print(f'ID de la Editorial -> {editorial[0]}')
                print(f'Nombre de la Editorial -> {editorial[1]}')
                print(f'Estado de la Editorial -> {editorial[2]}')
                print('***********************************')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')
    
    def buscar(self):
        try:
            id_editorial = input('Ingrese el codigo del Editorial -> ')
            where = {
                'id_editorial' : id_editorial
            }
            editorial = self.editorial.get_editorial(where)
            print('***********************************')
            print(f'ID de la Editorial -> {editorial[0]}')
            print(f'Nombre de la Editorial -> {editorial[1]}')
            print(f'Estado de la Editorial -> {editorial[2]}')
            print('***********************************')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def registrar(self):
        try:
            print('REGISTRO DE NUEVO EDITORIAL')
            editorial = input('Ingrese el nombre del Editorial -> ')
            data = {
                'editorial' : editorial,
                'estado' : True
            }
            self.editorial.insert_editorial(data)
            print('EDITORIAL REGISTRADO CORRECTAMENTE')

        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def actualizar(self):
        try:
            print('ACTUALIZAR EDITORIAL')
            id_editorial = input('Ingerse el ID de la Editorial a Actualizar -> ')
            editorial = input('Ingrese el nombre del Editorial -> ')
            estado = input('Ingrese el estado del Autor (Disponible -> True / No Disponible -> False) -> ')
            where = {
                'id_editorial' : id_editorial
            }
            data = {
                'editorial' : editorial,
                'estado' : estado
            }
            self.editorial.update_editorial(where, data)
            print('EDITORIAL ACTUALIZADO CORRECTAMENTE')
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

    def eliminar(self):
        try:
            print('ELIMINAR EDITORIAL')
            id_editorial = input('Ingrese el ID del Editorial a Eliminar -> ')
            where = {
                'id_editorial' : id_editorial
            }
            self.editorial.delete_editorial(where)
        except Exception as ex:
            print(f'Error encontrado: Code -> {str(ex)}')

        
            


        