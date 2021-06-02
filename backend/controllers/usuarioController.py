from connection.conn import Connection

class UsuarioRepo:

    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        

    def val_usuario(self, user, clave):
        try:
            conn = Connection('usuarios')
            records = conn.validacion(user,clave)
            
            for record in records:
                #print(f'Codigo: {record[0]}')
                #print('=====================')
                respuesta = {record[0]}

            if respuesta == {1}:
                print("INICIO DE SESION CORRECTO")
            else:
                print("INICIO DE SESION INCORRECTO, VALIDAR USUARIO/CONTRASEÑA")
            return respuesta
        except Exception as e:
            print(e)
    
