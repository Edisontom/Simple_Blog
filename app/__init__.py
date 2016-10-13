import ConfigParser
from flask import Flask
import os


directory_path = os.path.dirname(__file__)
config_path = os.path.join(directory_path, 'config.ini')
config = ConfigParser.ConfigParser()
config.read(config_path)

app.config.update( DATABASE = config.get('PATHS', 'db'),
                   SECRET_KEY = config.get('SECRETS', 'key'),
                   USERNAME = config.get('SECRETS', 'username'),
                   PASSWORD = config.get('SECRETS', 'password')
                      )
                      

