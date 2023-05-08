from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'localhost'
mysql = MySQL()

@app.route('/')
def Index():
    return 'Hello world'


@app.route('/add_contact')
def add_contact():
    return 'Add contact'


@app.route('/edit')
def edit_contact():
    return 'Edit contact'


@app.route('/delete')
def delete_contact():
    return 'Delete contact'


if __name__=='__main__':
    app.run(port=8000, debug=True)