import random
import sqlite3
from sqlite3 import Error
from faker import Faker

fake = Faker()

def create_connection(db_file):
    connection = None
    
    try:

        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM Athletes"
        )
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        
        connection.close()
        print(connection.total_changes)
        return connection
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

    return connection

create_connection(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")