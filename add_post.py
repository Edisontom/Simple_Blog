from ..db import get_db
from app import app
from flask import request, redirect, session,  abort, flash, url_for

@app.route('/add_post', methods=['POST'])
def add_post():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries(title, text) values(?, ?)',
        [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted' )
    return redirect(url_for('show_entries'))
