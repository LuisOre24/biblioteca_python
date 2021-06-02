from time import sleep
from controllers.lectorController import *

class Lector (LectorRepo):
    
    #CONSTRUCTOR
    def __init__(self, nombres):
        self.nombres = nombres

    #INTERFAZ CON EL USUARIO
    def interfazLector(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA LECTORES=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR A UN NUEVO LECTOR
            2 -> LISTAR LECTORES REGISTRADOS
            3 -> DESHABILITAR LECTOR
            4 -> ACTUALIZAR LECTOR
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_lector()
            elif respuesta == "2":
                self.listLector()
            elif respuesta == "3":
                self.deshabilitar_lector()
            elif respuesta == "4":
                self.actualizar_lector()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_lector(self):

        try:
            print('''REGISTRO DE LECTORES
                POR FAVOR INGRESE LOS NOMBRES, APELLIDOS, DNI, TELEFONO, DOMICILIO DEL LECTOR
            ''')
            nombre = input(">>Ingresar los nombres del Lector: >>> ")
            apellidos = input(">>Ingresar el apellidos paterno del Lector: >>> ")
            dni = input(">>Ingresar dni del Lector: >>> ")
            telefono = input(">>Ingresar el telefono del Lector: >>> ")
            domicilio = input(">>Ingresar el domicilio del Lector: >>> ")
            
            registro = {
                'nombres' : nombre,
                'apellidos' : apellidos,
                'dni' : dni,
                'telefono' : telefono,
                'domicilio' : domicilio,
                'estado' : True
            }

            self.insert_lector(registro)
            print("Lector registrado correctamente!")
            sleep(2)
            print("volviendo al menu Lectores")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazLector()

        except Exception as ex:
            print(f'Error al registrar al Lector. Error code: {str(ex)}')

    def listLector(self):
        self.all_lectores()

    def actualizar_lector(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR LECTORES A MODIFICAR              ")
            print("*****************************************************")
            self.all_lectores()
            id = input("Ingrese el ID del Lector a modificar: \n>>> ")
            where = {
                'id_lector' : id
            }
            
            lector = self.one_lector(where)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            nombres = input(f'Nombres: {lector[1]} >>> ')
            apellidos = input(f'Apellidos: {lector[2]} >>> ')
            dni = input(f'DNI: {lector[3]} >>> ')
            telefono = input(f'Telefono: {lector[4]} >>> ')
            domicilio = input(f'Domicilio: {lector[5]} >>> ')
            estado = input(f'Estado: {lector[6]} >>> ')

            registro = {
                'nombres' : nombres,
                'apellidos' : apellidos,
                'dni' : dni,
                'telefono' : telefono,
                'domicilio' : domicilio,
                'estado' : estado
            }

            self.update_lector(where, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Lector. Error code: {str(ex)}')

    def deshabilitar_lector(self):
        try:
            print("******************************************")
            print("       LISTA DE ALUMNOS REGISTRADOS       ")
            self.lectores_habilitados()
            print("******************************************")
            id = input(f'''
                POR FAVOR INGRESE EL ID DEL LECTOR A INHABILITAR
            ''')

            estado = 'false'
            data = {
                'id_lector' : id
            }
            self.inhabilitar_lector(estado, data)

            print(f'Lector indentificado con ID: {id} fue inhabilitado correctamente')

        except Exception as ex:
            print(f'Error al inhabilitar al lector, error code: {str(ex)}')


