#! /usr/bin/python

from options import setup_options

#from options import AgendaOptions
#from agenda_memory import AgendaMemory
#from agenda_database import AgendaDatabase
#from agenda_gtk import AgendaWindow
#import agenda_gtk


#print setup_options.moptions

if setup_options.getRunAs() == "terminal":
    #agendaDatabase = AgendaDatabase()
    #agendaDatabase.init_agenda()
    print "terminal"
elif setup_options.getRunAs() == "gtk":
    #agenda = AgendaWindow()
    #agenda.start_up()
    print "gtk"
    
else:
    print "There is none run as option available"

