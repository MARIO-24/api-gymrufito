import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        cursorclass=DictCursor,
        ssl_ca=None,
        ssl_disabled=False,
        ssl_verify_cert=False
    )