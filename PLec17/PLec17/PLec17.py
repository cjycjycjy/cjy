from flask import Flask, url_for,redirect,request,session,g,abort,render_template,flash
import sqlite3
from contextlib import closing

#configuration
DATABASE = 'flask.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)

#@app.route('/profile/<username>')
#def hello_world(username):
#    return "Hello " +username

#@app.route('/')
#def hello_world():
#    return redirect(url_for('login'))

#@app.route('/login')
#def login():
#    return "login"

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    db = connect_db()
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
    db.commit()
#init_db()
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title,text from entries order by id desc')
    entries = [dict(title = row[0], text = row[1]) for row in cur.fetchall()]
    #print(entries)
    return render_template('show_entries.html', entries = entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',[request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))



if __name__ == '__main__':
    #app.run()
    #app.debug = True
    app.run(host='203.252.166.23',port=5000)
