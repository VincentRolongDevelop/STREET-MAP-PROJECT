from flask import Flask
from psycopg2 import connect
from connection import connection
from routes import api
from service import map

#LUIFER BRANCH

app = Flask(__name__)

@app.get('/')
def home():
    conn= connection.get_connection()
    return 'Hello World'

"""  cur= conn.cursor()
cur.execute("SELECT 1 + 1")
result = cur.fetchone()
print (result) """

if __name__=='__main__':
    app.run(debug=True)

