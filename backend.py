import sqlite3
from sqlite3 import Error
from collections import namedtuple

Athlete = namedtuple('Athlete', [
    'id', 'first_name', 'last_name', 'age', 'acceleration', 'endurance', 
    'form', 'mental', 'speed', 'stamina', 'start', 'place', 'last_race_time', 
    'last_race_type', 'fastest_100m', 'fastest_200m', 'fastest_400m', 
    'races_ran', 'overall', 'overall_100m', 'overall_200m', 'overall_400m'
])

def add_athlete(first_name, last_name, age, acceleration, endurance, form, mental, speed, stamina, start):

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Athletes(first_name, last_name, age, acceleration, endurance, form, mental, speed, start)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, age, acceleration, endurance, form, mental, speed, stamina, start,)
        )
        connection.commit()
        
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
        athletes = [Athlete(*athlete) for athlete in cursor.fetchall()]
        return athletes

    except Error as e:
        print(e)
        
    finally:
        if connection:
            connection.close()

def search_athlete(id="", first_name="", last_name="", age="", acceleration="", endurance="", form="", mental="", speed="", stamina="", start="", overall="", overall_100m="", overall_200m="", overall_400m="", place="", last_race_time="", last_race_type="", fastest_100m="", fastest_200m="", fastest_400m="", races_ran=""):

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM Athletes WHERE id=? OR first_name=? OR last_name=? OR age=? OR acceleration=? OR endurance=? OR form=? OR mental=? OR speed=? OR stamina=? OR start=? OR overall=? OR overall_100m=? OR overall_200m=? OR overall_400m=? OR place=? OR last_race_time=? OR last_race_type=? OR fastest_100m=? OR fastest_200m=? OR fastest_400m=? OR races_ran=?"
            , (id, first_name, last_name, age, acceleration, endurance, form, mental, speed, stamina, start, overall, overall_100m, overall_200m, overall_400m, place, last_race_time, last_race_type, fastest_100m, fastest_200m, fastest_400m, races_ran,)
        )
        athletes = cursor.fetchall()

        if athletes:
            athletes = [Athlete(*athlete) for athlete in athletes]
            return athletes
    
    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()

def get_athlete(id):

    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM Athletes WHERE id=?"
            , (id,)
        )
        athlete_data = cursor.fetchone()

        if athlete_data:
            return Athlete(*athlete_data)
    
    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()

def update_athlete(id, first_name="", last_name="", age="", acceleration="", endurance="", form="", mental="", speed="", stamina="", start="", place="", last_race_time="", last_race_type="", fastest_100m="", fastest_200m="", fastest_400m="", races_ran=""):
    try:
        connection = sqlite3.connect(r"C:/Users/write/OneDrive/Documents/dk/tracksim/track-simulator/track.db")
        cursor = connection.cursor()
        
        # Check if the athlete with the given id exists
        cursor.execute("SELECT id FROM Athletes WHERE id=?", (id,))
        existing_id = cursor.fetchone()
        
        if existing_id:
            # Construct the SET clause dynamically based on provided parameters
            params = []
            set_clause_parts = []
            for attr, value in [("first_name", first_name), ("last_name", last_name), ("age", age), ("acceleration", acceleration), ("endurance", endurance), ("form", form), ("mental", mental), ("speed", speed), ("stamina", stamina), ("start", start), ("place", place), ("last_race_time", last_race_time), ("last_race_type", last_race_type), ("fastest_100m", fastest_100m), ("fastest_200m", fastest_200m), ("fastest_400m", fastest_400m), ("races_ran", races_ran)]:
                if value != "":
                    set_clause_parts.append(f"{attr}=?")
                    params.append(value)
            set_clause = ", ".join(set_clause_parts)
            
            # Append the id parameter to the end
            params.append(id)
            sql_statement = f"UPDATE Athletes SET {set_clause} WHERE id=?"
            
            # Execute the SQL statement with the provided values
            cursor.execute(sql_statement, params)
            connection.commit()
        else:
            print(f"Athlete with id {id} not found.")

    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()
