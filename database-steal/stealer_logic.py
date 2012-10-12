#! /usr/bin/python

from db_proyecto import ConectorSqlite
from db_proyecto import TablasSqlite
from classes_proyecto import Conector
from classes_proyecto import Tabla
from options import setup_options
import cx_Oracle
from datetime import datetime

class StealerLogic(object):
    
    def __init__(self):
        
        self.conector_db = ConectorSqlite()
        self.tablas_db = TablasSqlite()
        
    def populate_tables(self, projectId):
        """ 
        Mido el tiempo del script - INICIO
        """
        a = datetime.now()
        print a
        quantity_connectors = self.conector_db.retrieveAllCount(projectId)
        if quantity_connectors != 2:
            raise "It must have two connectors"
            
        else:
            self.tablas_db.delete_element(projectId)
            
            conectores = self.conector_db.selectAll(projectId, 2, 1)
            master = None
            slave = None
            for conector in conectores:
                if conector.master == 0:
                    slave = conector.getConnectionString()
                elif conector.master == 1:
                    master = conector.getConnectionString()
            
            print master
            print slave
            
            master_connection = cx_Oracle.connect(master)
            master_connection.clientinfo = 'python 2.7.3 @ rsantellan'
            master_connection.module = 'Master database stealer'
            master_connection.action = 'Master database stealer selects'
            print ("Master Oracle DB version: " + master_connection.version)
            print ("Master Oracle client encoding: " + master_connection.encoding)
            
            slave_connection = cx_Oracle.connect(master)
            slave_connection.clientinfo = 'python 2.7.3 @ rsantellan'
            slave_connection.module = 'Master database stealer'
            slave_connection.action = 'Master database stealer selects'
            print ("Slave Oracle DB version: " + slave_connection.version)
            print ("Slave Oracle client encoding: " + slave_connection.encoding)
            """ 
            Creo el cursor.
            """
            master_cursor = master_connection.cursor()
            slave_cursor = slave_connection.cursor()

            """ 
            Selecciono todas las tablas que corresponden a ese usuario
            """
            query_all_tables = "SELECT table_name FROM user_tables"
            
            master_cursor.execute(query_all_tables)
            
            rows_all_tables = master_cursor.fetchall()
            
            for row in rows_all_tables:
                
                #Have to calculate how many register the table have
                master_global_count = "SELECT COUNT(*) FROM %s" % row[0];
                master_cursor.execute(master_global_count)
                rowQuantity = master_cursor.fetchone()
                aux = Tabla()
                aux.proyecto_id = projectId
                aux.name = row[0]
                aux.quantity_master = int(rowQuantity[0])
                checked = False
                try:
                    
                    #Checking that in the database exists
                    slave_cursor.execute(master_global_count)
                    rowQuantitySlave = slave_cursor.fetchone()
                    checked = True
                except Exception, e:
                    print e
                     
                aux.checked = checked
                #check that in the other 
                self.tablas_db.insert_element(aux)
                
            
            master_connection.close()
            slave_connection.close()
                
            
        """ 
            Mido el tiempo del script - FIN
        """
        b = datetime.now()
        print b

        c = b - a
        print c
            
            
