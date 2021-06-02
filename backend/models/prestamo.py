from models.libro import Libro
from controllers.lectorController import LectorRepo
from time import sleep
from controllers.prestamoController import *
from datetime import date, datetime

class Prestamo (PrestamoRepo,LectorRepo):
    
    #CONSTRUCTOR
    def __init__(self, librito):
        self.librito = librito

    #INTERFAZ CON EL USUARIO
    def interfazPrestamo(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA PRESTAMOS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR A UN NUEVO PRESTAMO
            2 -> LISTAR PRESTAMOS REGISTRADOS
            3 -> DESHABILITAR PRESTAMO
            4 -> ACTUALIZAR PRESTAMO
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_prestamo()
            elif respuesta == "2":
                self.listPrestamo()
            elif respuesta == "3":
                self.deshabilitar_prestamo()
            elif respuesta == "4":
                self.actualizar_prestamo()
            elif respuesta == "5":
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_prestamo(self):

        try:
            print('''REGISTRO DE PRESTAMOS
                POR FAVOR INGRESE EL LIBRO, LECTOR, FECHA DE DEVOLUCION
            ''')
            libro_id = input(">>Ingresar ID del Libro a prestar: >>> ")
            id = {
                'id_libro' : libro_id
            }
            print(libro_id)
            libro = Libro().get_libro(id)
            if (libro[6] == True):
                lector = int(input(">>Ingresar el ID del Lector: >>> "))
                id_lector = {
                    'id_lector' : lector
                }
                getLector = self.get_lector(id_lector)
                if (getLector):
                    fecha_prestamo = datetime.now()
                    fecha = input(">>Ingresar la fecha de devolucion(dd/mm/yyyy): >>> ")
                    formato = "%d/%m/%Y"
                    var = datetime.strptime(fecha,formato)
                    año = var.year
                    mes = var.month
                    dia = var.day
                    fecha_devolucion = date(año,mes,dia)
                    registro = {
                        'id_libro' : libro_id,
                        'id_lector' : lector,
                        'fecha_prestamo' : fecha_prestamo,
                        'fecha_devolucion' : fecha_devolucion,
                        'estado' : True
                    }
                    libro_where = {
                        'id_libro' : libro_id
                    }
                    libro_update = {
                        'estado' : False
                    }
                    self.insert_prestamo(registro)
                    Libro().update_libro(libro_where,libro_update)
                    print("Prestamo registrado correctamente!")
                    sleep(2)
                    print("volviendo al menu Prestamos")
                    print("3")
                    sleep(1)
                    print("2")
                    sleep(1)
                    print("...")
                    self.interfazPrestamo()
                else:
                    print('El Lector no esta registrado; por favor primero registre al lector')
            else:
                print(f'El libro {libro_id} no esta disponible, elija otro libro porfavor')
                sleep(1)
                self.interfazPrestamo()

        except Exception as ex:
            print(f'Error al registrar el Prestamo. Error code: {str(ex)}')

    def listPrestamo(self):
        self.all_prestamos()

    def actualizar_prestamo(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR PRESTAMOS A MODIFICAR              ")
            print("*****************************************************")
            self.all_lectores()
            id = input("Ingrese el ID del Prestamo a modificar: \n>>> ")
            where = {
                'id_prestamo' : id
            }
            
            prestamo = self.one_prestamo(where)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            libro = int(input(f'Libro: {prestamo[1]} >>> '))
            lector = int(input(f'Lector: {prestamo[2]} >>> '))
            fecha_prestamo = {prestamo[3]} 
            fecha = input(f'Fecha Devolucion (dd/mm/YYYY): {prestamo[4]} >>> ')
            formato = "%d/%m/%Y"
            var = datetime.strptime(fecha,formato)
            año = var.year
            mes = var.month
            dia = var.day
            fecha_devolucion = date(año,mes,dia)
            estado = input(f'Estado: {prestamo[5]} >>> ')

            registro = {
                'id_libro' : libro,
                'id_lector' : lector,
                'fecha_prestamo' : fecha_prestamo,
                'fecha_devolucion' : fecha_devolucion,
                'estado' : estado
            }

            self.update_prestamo(where, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Prestamo. Error code: {str(ex)}')

    def deshabilitar_prestamo(self):
        try:
            id_libro = input('Ingrese el ID del Libro a devolver -> ')
            id = {
                'id_libro' : id_libro
            }
            libro = Libro().get_libro(id)
            if (libro[6] == False):
                estado = {
                    'estado' : True
                }
                Libro().update_libro(id, estado)
                print('Devolucion aceptada')
            else:
                print('El libro ingresado no ha sido prestado, ingrese correctamente el codigo del libro a devolver')
        except Exception as ex:
            print(f'ocurrio un error: code: {str(ex)}')

