#! /usr/bin/python
import yaml

class AgendaOptions(object):
    
    def __init__(self):
        configFile = open('options.yml')
        self.moptions = yaml.load(configFile)
        configFile.close()
        
    def getDatabaseType(self):
        return self.moptions['databases']['type']
        
    def getRunAs(self):
        return self.moptions['program']['run_as']
        
    def getSqliteDatabase(self):
        return self.moptions['databases']['sqlite3']['name']
        
    def getLimit(self):
        return self.moptions['databases']['limit']
    
    def getMysqlHost(self):
        return self.moptions['databases']['mysql']['host']

    def getMysqlUser(self):
        return self.moptions['databases']['mysql']['user']
        
    def getMysqlPass(self):
        return self.moptions['databases']['mysql']['pass']        

    def getMysqlSchema(self):
        return self.moptions['databases']['mysql']['schema']
                
setup_options = AgendaOptions()

