#! /usr/bin/python

class Proyecto(object):
    
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.descripcion = ""
        
    def __str__(self):
        return self.nombre
        


class Tabla(object):
    
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
        return "[{0}] Master: {1} Slave {2} | Use all: {3} | Condition: '{4}'".format(self.name, self.quantity_master, self.quantity_slave, self.use_all, self.condition)
        
class Conector(object):
    
    def __init__(self):
        self.id = 0
        self.proyecto_id = 0
        self.tipo = 0
        self.host = ""
        self.port = 0
        self.user = ""
        self.password = ""
        self.schema = ""
        self.master = 0
    
    def types(self):
        return {1: 'Oracle', 2: 'Mysql', 3: 'Sqlite'}
        
    def __str__(self):
        return "{0}:{1}/{2} User - {3} [Master: {4}]".format(self.host, self.port, self.schema, self.user, self.master)
        
    def getConnectionString(self):
        
        return "{0}/{1}@{2}:{3}/{4}".format(self.user, self.password, self.host, self.port, self.schema)
        
