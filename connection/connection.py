from psycopg2 import connect

host = 'localhost'
port = 5433
dbname = 'map'
user = 'postgres'
password = 123456

def get_connection():
    conn = connect(host=host,port=port,dbname=dbname,user=user,password=password)
    return conn