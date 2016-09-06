from flask import render_template
from app import app
from..db import get_db


@app.route( '/' )
def show_entries():
   db = get_db()
   cur = db.execute( 'select title, text from entries order by id desc' )
   entries = cur.fetchall()
   return render_template( 'show_entries.html' , entries=entries)