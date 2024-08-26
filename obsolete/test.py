import configparser as ConfigParser
import os

configParser = ConfigParser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), 'config.cfg')
configParser.read(configFilePath)
address = configParser.get("info","address")
print(address)