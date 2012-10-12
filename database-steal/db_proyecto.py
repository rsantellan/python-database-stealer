#! /usr/bin/python

import sqlite3
from options import setup_options
from classes_proyecto import Proyecto
from classes_proyecto import Conector
from classes_proyecto import Tabla

class BasicDbSqlite(object):
    
    def __init__(self):
        self.db = setup_options.getSqliteDatabase()
        
    def execute_query(self, sql, parameters):
        conn = None 
        lid = 0
        try:
            conn = sqlite3.connect(self.db)
            cur = conn.cursor()
            cur.execute(sql, parameters)
            conn.commit()
            lid = cur.lastrowid
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        return lid
        
    def execute_scalar(self, sql, parameters):
        conn = None 
        aux = None
        try:
            conn = sqlite3.connect(self.db)
            cur = conn.cursor()
            cur.execute(sql, parameters)
            aux = cur.fetchone()
            
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        return aux
        
    def execute_select(self, sql, parameters):
        conn = None 
        aux = []
        try:
            conn = sqlite3.connect(self.db)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(sql, parameters)
            aux = cur.fetchall()
            
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        return aux

    def execute_select_one(self, sql, parameters):
        conn = None 
        aux = None
        try:
            conn = sqlite3.connect(self.db)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(sql, parameters)
            aux = cur.fetchone()
            
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        return aux        
    

class ProyectoSqlite(BasicDbSqlite):
    
    
    def insert_element(self, element):
        
        sql = "INSERT INTO proyectos(nombre, descripcion) VALUES (:nombre, :descripcion)"
        params = {'nombre' : element.nombre, 'descripcion': element.descripcion}
        
        return super(ProyectoSqlite, self).execute_query(sql, params)
    

    def update_element(self, element):
        
        sql = "UPDATE proyectos SET nombre = :nombre, descripcion = :descripcion WHERE id = :id"
        params = {'nombre' : element.nombre, 'descripcion': element.descripcion, 'id': element.id}
        
        super(ProyectoSqlite, self).execute_query(sql, params)
        
    def delete_element(self, element):
        
        sql = "DELETE FROM proyectos WHERE id = :id"
        params = {'id': element.id}
        
        super(ProyectoSqlite, self).execute_query(sql, params)        
        
        
    def retrieveAllCount(self):
        sql = "SELECT count(id) FROM proyectos"
        params = {}
        aux = super(ProyectoSqlite, self).execute_scalar(sql, params)
        quantity = 0
        try:
            quantity = int (aux[0])
        except Exception, e:
            print "Error %s" % e.args[0]
        return quantity
        
        
    def selectAll(self, limit, page):
        
        return_list = []
        offset = (limit * page) - limit
        sql = "SELECT id, nombre, descripcion FROM proyectos ORDER BY id LIMIT :limit OFFSET :offset"
        params = {'limit' : limit, 'offset' : offset}
        list_aux = super(ProyectoSqlite, self).execute_select(sql, params)
        for row in list_aux:
            aux = self.hidratateObject(row)
            return_list.append(aux)
            
        return return_list
        
    def findOne(self, elementId):
        sql = "SELECT id, nombre, descripcion FROM proyectos WHERE id = :id"
        params = {'id' : elementId}
        aux = None
        row = super(ProyectoSqlite, self).execute_select_one(sql, params)
        try:
            aux = self.hidratateObject(row)
        except Exception, e:
            print "Error %s" % e.args[0]
        return aux
        
    def hidratateObject(self, row):
        aux = Proyecto()
        aux.id = row["id"]
        aux.nombre = row["nombre"]
        aux.descripcion = row["descripcion"]
        return aux


class ConectorSqlite(BasicDbSqlite):
    
    
    def insert_element(self, element):
        
        sql = "INSERT INTO conectores(proyecto_id, tipo, host, port, user, password, schema, master) VALUES (:proyecto_id, :tipo, :host, :port, :user, :password, :schema, :master)"
        params = {'proyecto_id' : element.proyecto_id, 'tipo': element.tipo, 'host': element.host, 'port': element.port, 'user': element.user, 'password': element.password, 'schema': element.schema, 'master': element.master}
        
        return super(ConectorSqlite, self).execute_query(sql, params)
    

    def update_element(self, element):
        
        sql = "UPDATE conectores SET nombre = :nombre, descripcion = :descripcion WHERE id = :id"
        params = {'nombre' : element.nombre, 'descripcion': element.descripcion, 'id': element.id}
        
        super(ConectorSqlite, self).execute_query(sql, params)
        
    def delete_element(self, element):
        
        sql = "DELETE FROM conectores WHERE id = :id"
        params = {'id': element.id}
        
        super(ConectorSqlite, self).execute_query(sql, params)        
        
        
    def retrieveAllCount(self, projectId):
        sql = "SELECT count(id) FROM conectores WHERE proyecto_id = :id"
        params = {'id': projectId}
        aux = super(ConectorSqlite, self).execute_scalar(sql, params)
        quantity = 0
        try:
            quantity = int (aux[0])
        except Exception, e:
            print "Error %s" % e.args[0]
        return quantity
        
        
    def selectAll(self, projectId, limit, page):
        
        return_list = []
        offset = (limit * page) - limit
        sql = "SELECT id, proyecto_id, tipo, host, port, user, password, schema, master FROM conectores WHERE proyecto_id = :id ORDER BY id LIMIT :limit OFFSET :offset"
        params = {'id': projectId, 'limit' : limit, 'offset' : offset}
        list_aux = super(ConectorSqlite, self).execute_select(sql, params)
        for row in list_aux:
            aux = self.hidratateObject(row)
            return_list.append(aux)
            
        return return_list
        
    def findOne(self, elementId):
        sql = "SELECT id, nombre, descripcion FROM conectores WHERE id = :id"
        params = {'id' : elementId}
        aux = None
        row = super(ConectorSqlite, self).execute_select_one(sql, params)
        try:
            aux = self.hidratateObject(row)
        except Exception, e:
            print "Error %s" % e.args[0]
        return aux
        
    def hidratateObject(self, row):
        aux = Conector()
        aux.id = row["id"]
        aux.proyecto_id = row["proyecto_id"]
        aux.tipo = row["tipo"]
        aux.host = row["host"]
        aux.port = row["port"]
        aux.user = row["user"]
        aux.password = row["password"]
        aux.schema = row["schema"]
        aux.master = row["master"]
        return aux

class TablasSqlite(BasicDbSqlite):
    
    
    def insert_element(self, element):
        
        sql = "INSERT INTO tablas(proyecto_id, name, checked, quantity_master, quantity_slave) VALUES (:proyecto_id, :name, :checked, :quantity_master, :quantity_slave )"
        params = {'proyecto_id' : element.proyecto_id, 'name': element.name, 'checked': element.checked, 'quantity_master': element.quantity_master, 'quantity_slave': element.quantity_slave}
        
        return super(TablasSqlite, self).execute_query(sql, params)
    

    def update_element(self, element):
        
        sql = "UPDATE tablas SET proyecto_id = :proyecto_id, name = :name, checked = :checked, quantity_master = :quantity_master, use_all = :use_all, condition = :condition WHERE id = :id"
        params = {'proyecto_id' : element.proyecto_id, 'name': element.name, 'checked': element.checked, 'quantity_master': element.quantity_master, 'quantity_slave': element.quantity_slave, 'use_all': element.use_all, 'condition' : element.condition, 'id': element.id}
        
        super(TablasSqlite, self).execute_query(sql, params)
        
    def delete_element(self, proyecto_id):
        
        sql = "DELETE FROM tablas WHERE proyecto_id = :id"
        params = {'id': proyecto_id}
        
        super(TablasSqlite, self).execute_query(sql, params)        
        
        
    def retrieveAllCount(self, proyecto_id):
        sql = "SELECT count(id) FROM tablas WHERE proyecto_id = :id"
        params = {'id': proyecto_id}
        aux = super(TablasSqlite, self).execute_scalar(sql, params)
        quantity = 0
        try:
            quantity = int (aux[0])
        except Exception, e:
            print "Error %s" % e.args[0]
        return quantity
        
        
    def selectAll(self, proyecto_id, limit, page):
        
        return_list = []
        offset = (limit * page) - limit
        sql = "SELECT id, proyecto_id, name, checked, quantity_master, quantity_slave, use_all, condition FROM tablas WHERE proyecto_id = :id ORDER BY name LIMIT :limit OFFSET :offset"
        params = {'id': proyecto_id, 'limit' : limit, 'offset' : offset}
        list_aux = super(TablasSqlite, self).execute_select(sql, params)
        for row in list_aux:
            aux = self.hidratateObject(row)
            return_list.append(aux)
            
        return return_list
        
    def findOne(self, elementId):
        sql = "SELECT id, proyecto_id, name, checked, quantity_master, quantity_slave, use_all, condition FROM tablas WHERE id = :id"
        params = {'id' : elementId}
        aux = None
        row = super(TablasSqlite, self).execute_select_one(sql, params)
        try:
            aux = self.hidratateObject(row)
        except Exception, e:
            print "Error %s" % e.args[0]
        return aux
        
    def selectAllVisible(self, proyecto_id):
        
        return_list = []
        offset = (limit * page) - limit
        sql = "SELECT id, proyecto_id, name, checked, quantity_master, quantity_slave, use_all, condition FROM tablas WHERE use_all = 1 AND proyecto_id = :id ORDER BY name"
        params = {'id': proyecto_id, 'limit' : limit, 'offset' : offset}
        list_aux = super(TablasSqlite, self).execute_select(sql, params)
        for row in list_aux:
            aux = self.hidratateObject(row)
            return_list.append(aux)
            
        return return_list
        
    def hidratateObject(self, row):
        aux = Tabla()
        aux.id = row["id"]
        aux.proyecto_id = row["proyecto_id"]
        aux.name = row["name"]
        aux.checked = row["checked"]
        aux.quantity_master = row["quantity_master"]
        aux.quantity_slave = row["quantity_slave"]
        aux.use_all = row["use_all"]
        aux.condition = row["condition"]
        return aux
