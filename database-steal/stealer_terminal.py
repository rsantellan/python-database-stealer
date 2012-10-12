#! /usr/bin/python

from sys import exit
from db_proyecto import ProyectoSqlite
from db_proyecto import ConectorSqlite
from db_proyecto import TablasSqlite
from classes_proyecto import Proyecto
from classes_proyecto import Conector
from classes_proyecto import Tabla
from options import setup_options
from stealer_logic import StealerLogic

class StealerTerminal(object):
    
    def __init__(self):
        self.proyectos_db = ProyectoSqlite()
        
    
    def list_proyectos(self, limit = setup_options.getLimit(), page = 1):
        print "======= Listing al projects ======="
        print "===========In case you want to delete a project press d plus the number =========================="
        quantity_proyectos = self.proyectos_db.retrieveAllCount()
        number = 1
        while number != 0:
            proyectos = self.proyectos_db.selectAll(limit, page)
            for proyecto in proyectos:
                print "{0}: {1}".format(proyecto.id, proyecto.nombre)
            
            if page > 1:
                print "To go to the previous page press < "
            
            if (page * limit) < quantity_proyectos:
                print "To go to the next page press > "
                
            option = raw_input("Select the number to edit or 0 to come back\n")
            try:
                if option == "<":
                    self.list_proyectos(limit, page - 1)
                    number = 0
                elif option == ">":
                    self.list_proyectos(limit, page + 1)
                    number = 0
                else:
                    number = int(option)
                    if number != 0:
                        self.proyecto_options(number)
                        
            except ValueError:
                print "It has to be a number"

    def proyecto_options(self, elementId):
        project = ProyectoTerminal(elementId, self.proyectos_db)
        project.start_up()
    
        
        
    def new_proyecto(self):
        print "========== Create a new project ================"
        aux = Proyecto()
        has_error = True
        name = ""
        while has_error:
            name = raw_input("[Name] > ")
            if name != "":
                has_error = False
        aux.nombre = name
        
        has_error = True
        description = ""
        while has_error:
            description = raw_input("[Description] > ")
            if name != "":
                has_error = False
        aux.descripcion = description
        aux.id = self.proyectos_db.insert_element(aux)
        
    def close_program(self):
        print "Thank you for using stealer 1.0.0"
        exit(0)

    
    def init_stealer(self):
        
        main_menu_text = {1 : 'Create new', 2: 'List', 3 : 'Exit'}
        main_menu_options = {1 : self.new_proyecto, 2: self.list_proyectos, 3 : self.close_program}

        options = { 'main' : { 'text' : main_menu_text, 'options' : main_menu_options}}
        start_point = 'main'

        selected = start_point
        print "========== Welcome to stealer 1.0.0 ================"

        while True:
            print "========== Main menu ================"
            displayed = options[selected]['text']
            sel_options = options[selected]['options']
        
            for k, v in displayed.iteritems():
                print " {0} - {1}".format(k, v)
            
            selection = raw_input("[Selection] >") 
            selection_int = 0
            try:
                #print selection
                selection_int = int(selection)
                function = sel_options[selection_int] 
                function()
            except ValueError:
                print "It has to be a number"
                
class ProyectoTerminal(object):
    
    def __init__(self, elementId, db):
        print "start"
        self.element_id = elementId
        self.proyectos_db = db
        self.conector_db = ConectorSqlite()
        self.tablas_db = TablasSqlite()
    
    def return_false(self):
        return False
                    
    def new_connection(self):
        print "========== Create a new connection ================"
        aux = Conector()
        aux.proyecto_id = self.element_id
        aux.tipo = 1
        
        has_error = True
        host = ""
        while has_error:
            host = raw_input("[Host] > ")
            if host != "":
                has_error = False
        aux.host = host
        
        has_error = True
        port = ""
        while has_error:
            port = raw_input("[Port] > ")
            if port != "":
                has_error = False
        aux.port = port
        
        has_error = True
        user = ""
        while has_error:
            user = raw_input("[User] > ")
            if user != "":
                has_error = False
        aux.user = user
        
        has_error = True
        password = ""
        while has_error:
            password = raw_input("[Password] > ")
            if password != "":
                has_error = False
        aux.password = password
        
        
        schema = ""
        schema = raw_input("[Schema] > ")
        aux.schema = schema
        
        has_error = True
        master = 0
        while has_error:
            try:
                aux_master = raw_input("[Master] > ")
                master = int(aux_master)
                if master == 0 or master == 1:
                    has_error = False
            except ValueError:
                print "It has to be a number" 
        aux.master = master
        
        aux.id = self.conector_db.insert_element(aux)
        return True

    def edit_table(self, tableId):
        aux = self.tablas_db.findOne(tableId)
        print "============== Editing table =================="
        print aux
        print "============ Choose options ==================="
        
        has_error = True
        use_all = 0
        while has_error:
            try:
                aux_master = raw_input("[Use all (1 for All and 0 for None)] > ")
                use_all = int(aux_master)
                if use_all == 0 or use_all == 1:
                    has_error = False
            except ValueError:
                print "It has to be a number" 
        aux.use_all = use_all
        
        
        condition = ""
        condition = raw_input("[Condition] > ")
        if condition != "":
            aux.condition = condition
        
        self.tablas_db.update_element(aux)
        
        print "Dont doing anything..."

    def populate_tables(self):
        stealLogic = StealerLogic()
        stealLogic.populate_tables(self.element_id)
        return True

    def edit_conector(self, conectorId):
        
        print "Dont doing anything..."
                
    def list_tables(self, limit = setup_options.getLimit(), page = 1):
        print "============= Listing tables =================="
        quantity_tables = self.tablas_db.retrieveAllCount(self.element_id)
        number = 1
        while number != 0:
            tablas = self.tablas_db.selectAll(self.element_id, limit, page)
            for tabla in tablas:
                print "{0}: {1}".format(tabla.id, tabla)
            
            if page > 1:
                print "To go to the previous page press < "
            
            if (page * limit) < quantity_tables:
                print "To go to the next page press > "
                
            option = raw_input("Select the number to edit or 0 to come back\n")
            try:
                if option == "<":
                    self.list_tables(limit, page - 1)
                    number = 0
                elif option == ">":
                    self.list_tables(limit, page + 1)
                    number = 0
                else:
                    number = int(option)
                    if number != 0:
                        self.edit_table(number)
                        
            except ValueError:
                print "It has to be a number"        
        
        return True

    def list_connection(self, limit = setup_options.getLimit(), page = 1):
        print "======= Listing conectors ======="
        print "===========In case you want to delete a project press d plus the number =========================="
        quantity_connectors = self.conector_db.retrieveAllCount(self.element_id)
        number = 1
        while number != 0:
            conectores = self.conector_db.selectAll(self.element_id, limit, page)
            for conector in conectores:
                print "{0}: {1}".format(conector.id, conector)
            
            if page > 1:
                print "To go to the previous page press < "
            
            if (page * limit) < quantity_connectors:
                print "To go to the next page press > "
                
            option = raw_input("Select the number to edit or 0 to come back\n")
            try:
                if option == "<":
                    self.list_connection(limit, page - 1)
                    number = 0
                elif option == ">":
                    self.list_connection(limit, page + 1)
                    number = 0
                else:
                    number = int(option)
                    if number != 0:
                        self.edit_conector(number)
                        
            except ValueError:
                print "It has to be a number"
        return True
                
    def start_up(self):
        aux = self.proyectos_db.findOne(self.element_id)
        if aux == None:
            print "Ups... None finded"
            return
        
        main_menu_text = {1 : 'Create connection', 2: 'List Connections', 3: 'Populate tables', 4: 'List tables', 5 : 'Back'}
        main_menu_options = {1 : self.new_connection, 2: self.list_connection, 3: self.populate_tables ,4 : self.list_tables, 5 : self.return_false}

        options = { 'main' : { 'text' : main_menu_text, 'options' : main_menu_options}}
        start_point = 'main'

        selected = start_point
        
        keep_going = True
        
        while keep_going:
            print "========== Project: {0} ================".format(aux.nombre)
            displayed = options[selected]['text']
            sel_options = options[selected]['options']
        
            for k, v in displayed.iteritems():
                print " {0} - {1}".format(k, v)
            
            selection = raw_input("[Selection] >") 
            selection_int = 0
            try:
                #print selection
                selection_int = int(selection)
                function = sel_options[selection_int] 
                keep_going = function()
            except ValueError:
                print "It has to be a number"        
        
