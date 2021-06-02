from time import sleep
from controllers.usuarioController import UsuarioRepo

class Usuario (UsuarioRepo):
    
    #CONSTRUCTOR
    def __init__(self, usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
  
    def ValSesion(self,user,clave):
        rpta = self.val_usuario(user,clave)
        return rpta

    