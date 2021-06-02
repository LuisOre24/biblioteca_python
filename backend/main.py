from models.usuario import Usuario
from models.prestamo import Prestamo
from controllers.libroController import LibroController
from controllers.autorController import AutorController
from controllers.editorialController import EditorialController
from models.lector import Lector
from models.usuario import Usuario
from models.libro import Libro
from time import sleep

class main(Lector, Prestamo, Usuario, Libro):

    def __init__(self):
        self.libro = LibroController()
        self.autor = AutorController()
        self.editorial = EditorialController()
        
        self.inicializer()

    def inicializer(self):

        user = input("INGRESE SU USUARIO: >> ")
        clv = input("INGRESE SU CONTRASEÑA: >> ")

        rpt = self.ValSesion(user,clv)
        
        if rpt == {1}:
         print("INICIO DE SESION CONFORME")   
         try:
             while True:
                 print('SISTEMA DE GESTION BIBLIOTECARIA')
                 print('''
                 1 .- PRESTAMO DE LIBRO
                 2 .- DEVOLUCION DE LIBRO
                 3 .- GESTIONAR LIBROS
                 4 .- GESTIONAR AUTORES
                 5 .- GESTIONAR EDITORIALES
                 6 .- GESTIONAR LECTOR
                 7 .- SALIR DEL SISTEMA
                 ''')
                 opcion = input('Ingrese una opcion -> ')
 
                 if(opcion == '1'):
                     self.interfazPrestamo()
                 elif(opcion == '2'):
                     self.deshabilitar_prestamo()
                 elif(opcion == '3'):
                     self.libro.inicio()
                 elif(opcion == '4'):
                     self.autor.inicio()
                 elif(opcion == '5'):
                     self.editorial.inicio()
                 elif(opcion == '6'):
                     self.interfazLector()
                 elif(opcion == '7'):
                     print('Gracias por usar el Sistema...')
                     sleep(2)
                     exit()
                 else:
                     print('ingrese una opcion valida')
 
         except KeyboardInterrupt:
             print('\n Se interrumpio la aplicación')
             
         except Exception as ex:
             print(str(ex))
        else:
            print("USUARIO O CONTRASEÑA INCORRECTA")
main()