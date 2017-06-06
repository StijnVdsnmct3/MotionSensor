from flask import Flask
from flask import render_template
from DbClass import DbClass
import os


app = Flask(__name__)


@app.route('/')
def login():
    render_template('login.html')

@app.route('/Home', methods=['post'])
def Homepage():
    error = None
    from flask import request

    username = request.form['uname']
    password = request.form['psw']

    do = DbClass()

    result = do.getuser(username, password)

    if result:
        return render_template('home.hmtl', role=result[3],)
    else:
        error = "Verkeerde Login"
        return render_template('login.html', error= error)


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