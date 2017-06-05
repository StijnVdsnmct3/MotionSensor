from flask import Flask
from flask import render_template
from DbClass import DbClass



app = Flask(__name__)


@app.route('/', methods=['post'])
def login():
    error = None
    from flask import request
    if request.method == 'post':
        username = request.form['uname']
        password = request.form['psw']

        do = DbClass()

        result = do.getuser(username,password)

        if result:
            return render_template('home.hmtl', role=result[3])
        else:
            error = "Verkeerde Login"
    render_template('login.html',error=error)

@app.route('/Home')
def Homepage():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
