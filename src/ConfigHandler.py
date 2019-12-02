# -*- coding: utf-8 -*-

import configparser

class ConfigHandler(object):

    def __init__(self, section=""):        
        self.path = 'settings.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.path)
        self.section = section     
        #print(self.config.sections())
        
    def setSection(self, section):
        self.section = section
        
    def getValue(self, option, section=''):
        if not section:
            section = self.section
        if not section:
            return False
        value = self.config[section][option]      
        return value.strip("'")
              
    def setValue(self, option, value):
        self.config.set(self.section, option, value)
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)        

# c = ConfigHandler("DataSource")
# s = c.getValue("source")
# print(s+s)
# print("hi")

