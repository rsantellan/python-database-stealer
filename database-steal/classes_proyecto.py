#! /usr/bin/python

class Proyectos(object):
    
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.descripcion = ""
        
    def __str__(self):
        return self.nombre


class Tablas(object):
    
    def __init__(self):
        self.id = 0
        self.proyecto_id = 0
        self.name = ""
        self.checked = False
        self.quantity_master = 0
        self.quantity_slave = 0
        self.use_all = False
        self.condition = ""
        
    def __str__(self):
        return self.name
        
class Conectores(object):
    
    def __init__(self):
        self.id = 0
        self.proyecto_id = 0
        self.tipo = 0
        self.host = ""
        self.port = 0
        self.user = ""
        self.password = ""
        self.schema = ""
    
    def types(self):
        return {1: 'Oracle', 2: 'Mysql', 3: 'Sqlite'}
        
