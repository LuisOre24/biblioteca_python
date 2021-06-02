from connection.conn import Connection

class LectorRepo:

    def __init__(self, nombres, apellidos, dni, telefono, domicilio):
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.telefono = telefono
        self.domicilio = domicilio
        

    def all_lectores(self):
        try:
            conn = Connection('lector')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombres: {record[1]}')
                print(f'Apellidos: {record[2]}')
                print(f'DNI: {record[3]}')
                print(f'Telefono: {record[4]}')
                print(f'Domicilio: {record[5]}')
                print(f'Estado: {record[6]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_lector(self,id):
        try:    
            conn = Connection('lector')
            records = conn.get_by_id(id)

            print(f'ID: {records[0]}')
            print(f'Nombres: {records[1]}')
            print(f'Apellidos: {records[2]}')
            print(f'DNI: {records[3]}')
            print(f'Telefono: {records[4]}')
            print(f'Domicilio: {records[5]}')
            print(f'Estado: {records[6]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def get_lector(self, id):
        conn = Connection('lector')
        return conn.get_by_id(id)
    
    def insert_lector(self, data):
        
        try:  
            conn = Connection('lector')
            conn.insert(data)

            print(f'se registro correctamente al lector')

        except Exception as ex:
            print(ex)


    def update_lector(self, id_object, data):

        conn = Connection('lector')

        list_where = []
        for field_name, field_value in id_object.items():
            if isinstance(field_value, str):
                field_value = f"'{field_value}'"
            list_where.append(f"{field_name}={field_value}")
        
        list_update = []
        for field_name, field_value in data.items():
            if isinstance(field_value, str):
                field_value = f"'{field_value}'"
            list_update.append(f"{field_name}={field_value}")
            
        query = f'''
            UPDATE {conn.table_name} SET {', '.join(list_update)}
            WHERE {' AND '.join(list_where)}
        '''
        conn.execute_query(query)
        return True

    def inhabilitar_lector(self,parameter, id_object):
        conn = Connection('lector')
        conn.disable(parameter, id_object)
        return True

    def lectores_habilitados(self):
        conn = Connection('lector')
        query = f'''
            SELECT * FROM {conn.table_name} WHERE estado = 'true'
        '''
        conn.cursor.execute(query)
        records = conn.cursor.fetchall()

        for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombres: {record[1]}')
                print(f'Apellido: {record[2]}')
                print(f'DNI: {record[3]}')
                print(f'Telefono: {record[4]}')
                print(f'Domicilio: {record[5]}')
                print(f'Estado: {record[6]}')
                print('=====================')
