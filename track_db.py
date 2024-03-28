import backend
import sqlite3

def get_athlete_info(athlete_id):
    connection = sqlite3.connect("your_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM athletes WHERE id=?", (athlete_id,))
    athlete_data = cursor.fetchone()
    connection.close()
    return athlete_data

def format_athlete_info(athlete_data):
    athlete_data = athlete_data[0]
    if athlete_data:
        athlete_info = (
            f"Name: {athlete_data[1]} {athlete_data[2]}, Age: {athlete_data[3]}, "
            f"Acceleration: {athlete_data[4]}, Endurance: {athlete_data[5]}, "
            f"Form: {athlete_data[6]}, Mental: {athlete_data[7]}, "
            f"Speed: {athlete_data[8]}, Stamina: {athlete_data[9]}, "
            f"Start: {athlete_data[10]}, Overall: {athlete_data[18]}, "
            f"100m Overall: {athlete_data[19]}, 200m Overall: {athlete_data[19]}, "
            f"400m Overall: {athlete_data[20]}, Races ran: {athlete_data[17]}, "
            f" Place in Last Race: {athlete_data[11]}, "
            f"Last Race Type: {athlete_data[12]}, Last Race Time: {athlete_data[13]}, "
            f"Fastest 100m: {athlete_data[14]}, Fastest 200m: {athlete_data[15]}, "
            f"Fastest 400m: {athlete_data[16]}"
        )
        return athlete_info
    else:
        return "Athlete not found."

athlete_id = "1"  # Change this to the ID of the athlete you want to retrieve info for
athlete_data = backend.search_athlete(athlete_id)
athlete_info_str = format_athlete_info(athlete_data)
print(athlete_info_str)

def game_loop():
    pass