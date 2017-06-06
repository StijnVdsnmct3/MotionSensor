from flask import Flask
from flask import render_template, redirect, url_for, session, abort, request
from DbClass import DbClass
import os


app = Flask(__name__)
app.secret_key = 'wa is dit'

@app.route('/')
def Index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def Login():
    username = request.form['uname']
    password = request.form['psw']
    do = DbClass()
    result = do.getuser(username,password)
    if result:
        session['logged_in'] = True
    else:
        session['logged_in'] = False
    return Index()

@app.route('/Home')
def Homepage():
    render_template('home.html')

@app.route('/Logs')
def Logs():
    do = DbClass()
    result = do.getlogs()
    return render_template('logs.html', logs=result)

@app.route('/Comments')
def comments():
    return render_template('comments.html')

@app.route('/commentsent', methods=['post'])
def commentsent():
    from flask import request

    naam = request.form['naam']
    voornaam = request.form['voornaam']
    bericht = request.form['comment']
    do = DbClass()
    do.setcomments(naam,voornaam,bericht)
    return render_template('commentsent.html')


if __name__ == '__main__':
    # app.run()
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=80,debug=True)