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
        insert_stmt = (
            "INSERT INTO Athletes(first_name, last_name, age, acceleration, endurance, form, mental, speed, start)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        )

        for i in range(99):
            data = (fake.unique.first_name_male(), fake.unique.last_name(), random.randint(15,30), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
            cursor.execute(insert_stmt, data)
            connection.commit()

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

# insert_stmt = (
#     "INSERT INTO Athletes(first_name, last_name, age, acceleration, endurance, form, mental, speed, start)"
#     "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
# )

# for i in range(99):
#     data = (fake.unique.first_name_male(), fake.unique.last_name(), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
#     cursor.execute(insert_stmt, data)
#     conn.commit()

# conn.close()