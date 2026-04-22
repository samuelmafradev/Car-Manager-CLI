import sqlite3
import os
# 1. Get connection.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "car_management.db")


def get_connection():
    return sqlite3.connect(db_path)
