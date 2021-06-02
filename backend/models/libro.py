from connection.conn import Connection


class Libro:
    def __init__(self):
        self.model = Connection('libro')

    def get_libros(self):
        return self.model.get_all()

    def get_libro(self, id_object):
        return self.model.get_by_id(id_object)

    def search_libro(self, data):
        return self.model.get_columns(data)

    def insert_libro(self, libro):
        return self.model.insert(libro)

    def update_libro(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_libro(self, id_object):
        return self.model.delete(id_object)