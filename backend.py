import sqlite3
from sqlite3 import Error

def add_athlete(first_name, last_name, age, acceleration, endurance, form, mental, speed, stamina, start):

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Athletes(first_name, last_name, age, acceleration, endurance, form, mental, speed, start)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, age, acceleration, endurance, form, mental, speed, stamina, start)
        )
        connection.commit()
        connection.close()
        
    except Error as e:
        print(e)
        
    finally:
        if connection:
            connection.close()

def view_athletes():

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM Athletes"
        )
        rows = cursor.fetchall()
        connection.close()
        return rows

    except Error as e:
        print(e)
        
    finally:
        if connection:
            connection.close()

def search_athlete(id="", first_name="", last_name="", age="", acceleration="", endurance="", form="", mental="", speed="", stamina="", start="", overall="", overall_100m="", overall_200m="", overall_400m=""):

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM Athletes WHERE id=? OR first_name=? OR last_name=? OR age=? OR acceleration=? OR endurance=? OR form=? OR mental=? OR speed=? OR stamina=? OR start=? OR overall=? OR overall_100m=? OR overall_200m=? OR overall_400m=?"
            , (id, first_name, last_name, age, acceleration, endurance, form, mental, speed, stamina, start, overall, overall_100m, overall_200m, overall_400m)
        )
        rows = cursor.fetchall()
        connection.close()
        return rows
    
    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()
#Unused
def get_athlete(id):

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM Athletes WHERE id=?"
            , (id)
        )
        athlete_data = cursor.fetchone()
        connection.close()
        return athlete_data
    
    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()

def update_athlete(id, first_name="", last_name="", age="", acceleration="", endurance="", form="", mental="", speed="", stamina="", start=""):

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Athletes SET first_name=?, last_name=?, age=?, acceleration=?, endurance=?, form=?, mental=?, speed=?, stamina=?, start=? WHERE id=?",
            (first_name, last_name, age, acceleration, endurance, form, mental, speed, stamina, start, id)
        )
        connection.commit()
        connection.close()

    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()

#print(get_athlete("2"))