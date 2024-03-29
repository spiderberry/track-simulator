import backend
import random
import numpy as np
from collections import namedtuple

def format_athlete_info(athlete_data):
    if athlete_data is None:
        return "Athlete not found."

    (athlete_id, first_name, last_name, age, acceleration, endurance, form, mental, 
     speed, stamina, start, place, last_race_time, last_race_type, fastest_100m, 
     fastest_200m, fastest_400m, races_ran, overall, overall_100m, overall_200m, 
     overall_400m) = athlete_data

    return (
        f"Name: {first_name} {last_name}, Age: {age}, "
        f"Acceleration: {acceleration}, Endurance: {endurance}, "
        f"Form: {form}, Mental: {mental}, Speed: {speed}, "
        f"Stamina: {stamina}, Start: {start}, Overall: {overall}, "
        f"100m Overall: {overall_100m}, 200m Overall: {overall_200m}, "
        f"400m Overall: {overall_400m}, Races ran: {races_ran}, "
        f"Place in Last Race: {place}, Last Race Type: {last_race_type}, "
        f"Last Race Time: {last_race_time}, Fastest 100m: {fastest_100m}, "
        f"Fastest 200m: {fastest_200m}, Fastest 400m: {fastest_400m}"
    )

    
def sort_race(runners_time, runners):

    runners_time.sort()

    for i in runners:
        for j in range(len(runners_time)):
            
            if i.last_race_time == runners_time[j]:
                i.place = j + 1

def one_hundred_meters(runner):
    
    runner
    mean100m = 10.7459527863
    sd100m = 0.133776557
    max_time = 8.00  # Maximum overall performance time
    overall = runner[19]

    # Adjusting mean and standard deviation based on overall performance
    mean = mean100m - (overall - 50) * (mean100m - max_time) / 50
    
    # Generating random time within the adjusted mean and standard deviation
    time = np.random.normal(mean, sd100m)
    
    return time

def one_hundred_meters_race(runners):
        
        runners_time = []
        winning_time = 15.00
        winner = None

        #Simulate race and find winner
        for runner in runners:
            runner_time = float(f"{one_hundred_meters(runner):.2f}")
            runners_time.append(runner_time)

            if runner_time < winning_time:
                winning_time = runner_time
                winner = f"{runner.first_name} {runner.last_name}"
        
        #Update the database records
        for runner, time in zip(runners, runners_time):
            backend.update_athlete(runner.id, last_race_time=time, last_race_type="100m")

            if time < runner.fastest_100m:
                backend.update_athlete(runner.id, fastest_100m=time)

            backend.update_athlete(runner.id, stamina=max(runner.stamina-10, 0))
            backend.update_athlete(runner.id, races_ran=(runner.races_ran+1))
        
        #Print the race results
        print(f"100m: {len(runners)} runners")
        print("------------------------------")
        for i, runner in enumerate(runners):
            print(f"Lane {i+1}: {runner.first_name} {runner.last_name} ran {runners_time[i]}. OVR: {runner.overall_100m}")

        print(f"The winner is {winner} with a time of {winning_time}")

        # Sort the race results if needed
        sort_race(runners_time, runners)
        
chosen_numbers = set()
runners = []

for i in range(8):
    while True:
        random_number = str(random.randint(1,99))
        if random_number not in chosen_numbers:
            chosen_numbers.add(random_number)
            break

    athlete = backend.get_athlete(random_number)
    print(athlete)
    runners.append(athlete)
runners2 = [backend.get_athlete(94), backend.get_athlete(2), backend.get_athlete(49), backend.get_athlete(58), backend.get_athlete(99), backend.get_athlete(7), backend.get_athlete(28), backend.get_athlete(40)]
print("Race time!")
print(runners)
one_hundred_meters_race(runners)

def game_loop():
    pass