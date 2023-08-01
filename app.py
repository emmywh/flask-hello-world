import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_db_user:MS4onYOvQbXEnFjclqB58lGj3OqTg7hZ@dpg-cj482iiip7vuasjndbeg-a/lab10_db")
    conn.close
    return "Database Connection Successful"
