import sqlite3
import os
from flask import Flask, g

DATABASE = '/tmp/app.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
DATABASE=os.path.join(app.root_path, 'app.db' ),
DEBUG=True,
SECRET_KEY= 'development key' ,
USERNAME= 'admin' ,
PASSWORD= 'default'
))
app.config.from_envvar( 'FLASKR_SETTINGS' , silent=True)


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def connect_db():
  rv = sqlite3.connect(app.config[ 'DATABASE' ])
  rv.row_factory = sqlite3.Row
  return rv

def init_db():
 with app.app_context():
   db = get_db()
   with app.open_resource( 'db/schema.sql' , mode= 'r' ) as f:
     db.cursor().executescript(f.read())
   db.commit()

