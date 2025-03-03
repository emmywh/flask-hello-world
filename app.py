import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_db_user:MS4onYOvQbXEnFjclqB58lGj3OqTg7hZ@dpg-cj482iiip7vuasjndbeg-a/lab10_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://lab10_db_user:MS4onYOvQbXEnFjclqB58lGj3OqTg7hZ@dpg-cj482iiip7vuasjndbeg-a/lab10_db") 
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgres://lab10_db_user:MS4onYOvQbXEnFjclqB58lGj3OqTg7hZ@dpg-cj482iiip7vuasjndbeg-a/lab10_db") 
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgres://lab10_db_user:MS4onYOvQbXEnFjclqB58lGj3OqTg7hZ@dpg-cj482iiip7vuasjndbeg-a/lab10_db") 
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.commit()
    conn.close()
    pro_athelte_table = ""
    # creates table
    pro_athelte_table+="<table>"
    # creates table row
    for pro_athlete in records:
        pro_athelte_table+="<tr>"
        # creates columns for pro athlete info
        for about in pro_athlete:
            pro_athelte_table+="<td>{}</td>".format(about)
        pro_athelte_table+="</tr>"
    # closes table
    pro_athelte_table+="</table>"
    return pro_athelte_table

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgres://lab10_db_user:MS4onYOvQbXEnFjclqB58lGj3OqTg7hZ@dpg-cj482iiip7vuasjndbeg-a/lab10_db") 
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"