import os
from dotenv import load_dotenv
import psycopg2
import sqlite3

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()

#Fetch RPG data
rpgconn = sqlite3.connect('rpg_db.sqlite3')