from flask import Flask, url_for,redirect

app = Flask(__name__)
#@app.route('/profile/<username>')
#def hello_world(username):
#    return "Hello " +username

@app.route('/')
def hello_world():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "login"


if __name__ == '__main__':
    #app.run()
    #app.debug = True
    app.run(host='203.252.166.23',port=5000)
