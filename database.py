import pymysql
from pymysql.cursors import DictCursor

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",  # tu contraseña
        database="gym_rufito",
        cursorclass=DictCursor
    )
