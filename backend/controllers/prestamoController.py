from connection.conn import Connection

class PrestamoRepo:

    def __init__(self, id_libro, id_lector, fecha_prestamo, fecha_devolucion):
        self.id_libro = id_libro
        self.id_lector = id_lector
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        
        

    def all_prestamos(self):
        try:
            conn = Connection('prestamo')
            records = conn.select([])
            
            for record in records:
                print(f'Libro: {record[0]}')
                print(f'Lector: {record[1]}')
                print(f'Fecha Prestamo: {record[2]}')
                print(f'Fecha Devolución: {record[3]}')
                print(f'Estado: {record[4]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_prestamo(self,id):
        try:    
            conn = Connection('prestamo')
            records = conn.selectOne(id)

            print(f'Libro: {records[0]}')
            print(f'Lector: {records[1]}')
            print(f'Fecha Prestamo: {records[2]}')
            print(f'Fecha Devolución: {records[3]}')
            print(f'Estado: {records[4]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_prestamo(self, data):
        
        try:  
            conn = Connection('prestamo')
            conn.insert(data)

            print(f'se registro correctamente el prestamo')

        except Exception as ex:
            print(ex)


    def update_prestamo(self, id_object, data):

        conn = Connection('prestamo ')

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

    def inhabilitar_prestamo(self,parameter, id_object):
        conn = Connection('prestamo')
        conn.disable(parameter, id_object)
        return True

    def prestamos_habilitados(self):
        conn = Connection('prestamo')
        query = f'''
            SELECT * FROM {conn.table_name} WHERE estado = 'true'
        '''
        conn.cursor.execute(query)
        records = conn.cursor.fetchall()

        for record in records:
                print(f'Libro: {record[0]}')
                print(f'Lector: {record[1]}')
                print(f'Fecha Prestamo: {record[2]}')
                print(f'Fecha Devolución: {record[3]}')
                print(f'Estado: {record[4]}')
                print('=====================')
