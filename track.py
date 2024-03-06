import random
import numpy as np

class Player:

    #Constructor with player attributes
    def __init__(self, name, age, acceleration, endurance, form, mental, speed, start):
        
        self.name = name
        self.age = age
        self.acceleration = acceleration
        self.endurance = endurance
        self.form = form
        self.mental = mental
        self.speed = speed
        self.stamina = 100
        self.start = start
        self.place = None
        self.last_race_time = None
        self.last_race_type = None
        self.fastest_100m = 15.0
        self.fastest_200m = 30.0
        self.fastest_400m = 60.0
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Acceleration: {self.acceleration}, Endurance: {self.endurance}, Form: {self.form}, Mental: {self.mental}, Speed: {self.speed}, Stamina: {self.stamina}, Start: {self.start}, Place: {self.place}, Last Race Type: {self.last_race_type}, Last Race Time: {self.last_race_time}, Fastest 100m: {self.fastest_100m}, Fastest 200m: {self.fastest_200m}, Fastest 400m: {self.fastest_400m}"
    
    #calculate 100m overall
    def overall_100m(self):

        #Weighing attributes based on race
        acceleration = 1.5 * self.acceleration
        speed = 1.5 * self.speed
        start = 1.25 * self.start
        form = self.form
        endurance = .75 * self.endurance
        stamina = .4 * self.stamina
        mental = .1 * self.mental

        ovr = acceleration + speed + start + form + endurance + stamina + mental

        max_score = 1.5 * 100 + 1.5 * 100 + 1.25 * 100 + 100 + 0.75 * 100 + 0.4 * 100 + 0.1 * 100

        scaled_ovr = int((ovr / max_score) * 100)

        return scaled_ovr
    
    #calculate 200m overall
    def overall_200m(self):

        #Weighing attributes based on race
        acceleration = 1.5 * self.acceleration
        speed = 2 * self.speed
        start = .3 * self.start
        form = self.form
        endurance = 1.30 * self.endurance
        stamina = .7 * self.stamina
        mental = .15 * self.mental

        ovr = acceleration + speed + start + form + endurance + stamina + mental

        max_score = 1.5 * 100 + 2 * 100 + .3 * 100 + 100 + 1.30 * 100 + 0.7 * 100 + 0.15 * 100

        scaled_ovr = int((ovr / max_score) * 100)

        return scaled_ovr
    
    #calculate 400m overall
    def overall_400m(self):

        #Weighing attributes based on race
        acceleration = .8 * self.acceleration
        speed = 1.1 * self.speed
        start = .2 * self.start
        form = 1.3 * self.form
        endurance = 2.5 * self.endurance
        stamina = .7 * self.stamina
        mental = .4 * self.mental

        ovr = acceleration + speed + start + form + endurance + stamina + mental

        max_score = .8 * 100 + 1.1 * 100 + .2 * 100 + 1.3* 100 + 2.5 * 100 + 0.7 * 100 + 0.4 * 100

        scaled_ovr = int((ovr / max_score) * 100)

        return scaled_ovr
    
class Players:

    import random

    def random_name_from_file():

        file_path = "names.txt"

        try:
            with open(file_path, 'r') as file:

                # Read names from the file and store them in a list
                names = [line.strip() for line in file]

            # Randomly select a name from the list
            random_name = random.choice(names)
            
            return random_name
        
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        
        except Exception as e:
            print("An error occurred:", e)
            return None

    def generate_random_characters(num_players, players):
        
        for i in range(num_players):

            # Initialize attributes
            name = Players.random_name_from_file()
            age = random.randint(18, 40)  # Adjusted to ensure ages between 18 and 40
            acceleration = 0
            endurance = 0
            form = 0
            mental = 0
            speed = 0
            start = 0
            
            remaining_points = 150

            # Assign points to attributes until no points remain
            while remaining_points > 0:

                # Randomly select an attribute to increase
                attribute = random.choice(["acceleration", "endurance", "form", "mental", "speed", "start"])

                # Randomly allocate points to the selected attribute, ensuring that it does not exceed the remaining points
                points_allocated = random.randint(0, min(remaining_points, 100))  # Maximum of 100 points per attribute

                # Update the attribute value and decrement the remaining points
                if attribute == "acceleration":
                    acceleration += points_allocated

                elif attribute == "endurance":
                    endurance += points_allocated

                elif attribute == "form":
                    form += points_allocated

                elif attribute == "mental":
                    mental += points_allocated

                elif attribute == "speed":
                    speed += points_allocated

                elif attribute == "start":
                    start += points_allocated
                    
                remaining_points -= points_allocated

            # Create a Player object with the generated attributes
            player = Player(name, age, acceleration, endurance, form, mental, speed, start)
            players.append(player)

        return players

    def _100_practice(player):

        #Random amount of xp
        xp = random.randint(1,5)
        xp2 = random.randint(1,3)
        xp3= random.randint(1,2)

        #Adding random xp
        player.acceleration = player.acceleration + xp
        player.speed = player.speed + xp2
        player.start = player.start + xp3
        player.stamina = player.stamina - 10

    def _200_practice(player):

        #Random amount of xp
        xp = random.randint(1,3)
        xp2 = random.randint(1,5)
        xp3= random.randint(1,2)

        #Adding random xp
        player.acceleration = player.acceleration + xp
        player.speed = player.speed + xp2
        player.endurance = player.endurance + xp3
        player.stamina = player.stamina - 10

    def _400_practice(player):

        #Random amount of xp
        xp = random.randint(1,5)
        xp2 = random.randint(1,3)
        xp3= random.randint(1,2)

        #Adding random xp
        player.endurance = player.endurance + xp
        player.form = player.form + xp2
        player.speed = player.speed + xp3
        player.stamina = player.stamina - 10

    def acceleration_practice(player):

        xp = random.randint(5,10)

        player.acceleration = player.acceleration + xp
        player.stamina = player.stamina - 5

    def endurance_practice(player):

        xp = random.randint(5,10)

        player.endurance = player.endurance + xp
        player.stamina = player.stamina - 5

    def form_practice(player):

        xp = random.randint(5,10)

        player.form = player.form + xp
        player.stamina = player.stamina - 5

    def mental_practice(player):

        xp = random.randint(5,10)

        player.mental = player.mental + xp
        player.stamina = player.stamina - 5

    def speed_practice(player):

        xp = random.randint(5,10)

        player.speed = player.speed + xp
        player.stamina = player.stamina - 5

    def start_practice(player):

        xp = random.randint(5,10)

        player.start = player.start + xp
        player.stamina = player.stamina - 5

class Tracksim():
    
    mean100m = 10.7459527863
    sd100m = 0.133776557
    mean200m = 21.52218721
    sd200m = 0.160942679
    mean400m = 44.8896305
    sd400m = 0.3135084355

    def sort_race(runners_time, runners):

        runners_time.sort()

        for i in runners:
            for j in range(len(runners_time)):
                
                if i.last_race_time == runners_time[j]:
                    i.place = j + 1

    def one_hundred_meters(runner):

        overall = runner.overall_100m()

        mean = Tracksim.mean100m -(overall - 50) * (3 * (Tracksim.sd100m *.3125)) / 50
        time = np.random.normal(mean, (Tracksim.sd100m *.3125))
        
        return time
    
    def two_hundred_meters(runner):

        overall = runner.overall_200m()

        mean = Tracksim.mean200m -(overall - 50) * (3 * (Tracksim.sd200m *.3125)) / 50
        time = np.random.normal(mean, (Tracksim.sd200m *.3125))
        
        return time
    
    def four_hundred_meters(runner):

        overall = runner.overall_400m()

        mean = Tracksim.mean400m -(overall - 50) * (3 * (Tracksim.sd400m *.3125)) / 50
        time = np.random.normal(mean, (Tracksim.sd400m *.3125))
        
        return time
    
    def one_hundred_meters_race(runners):
        
        runners_time = []
        winning_time = 15.00
        winner = None

        #Adds each time to runners_time list
        for i in runners:
            runners_time.append(float(f"{Tracksim.one_hundred_meters(i):.2f}"))

        #Finds fastest time and sets that to winning time and assigns the winner
        for i in range(len(runners_time)):
            
            if (runners_time[i] < winning_time):
                
                winning_time = runners_time[i]
                winner = runners[i].name

        #Updates runner's last race 
        for i in range(len(runners)):
            runners[i].last_race_time = runners_time[i]
            runners[i].last_race_type = "100m"

        #Updates runners fastest time if applicable
        for i in range(len(runners)):
            
            if runners_time[i] < runners[i].fastest_100m:
                runners[i].fastest_100m = runners_time[i]

        print(f"100m: {len(runners)} runners")
        print("------------------------------")
        
        for i in range(len(runners)):

            print(f"Lane {i+1}: {runners[i].name} ran {runners[i].last_race_time}. OVR: {runners[i].overall_100m()}")

        print(f"The winner is {winner} with a time of {winning_time}")

        for i in range(len(runners)):
            runners[i].stamina -= 10

        Tracksim.sort_race(runners_time, runners)
            
    def two_hundred_meters_race(runners):
        
        runners_time = []
        winning_time = 30.00
        winner = None

        #Adds times to runners_time list
        for i in runners:
            runners_time.append(float(f"{Tracksim.two_hundred_meters(i):.2f}"))

        #Finds fastest time and sets that to winning time and assigns the winner
        for i in range(len(runners_time)):
            
            if (runners_time[i] < winning_time):
                
                winning_time = runners_time[i]
                winner = runners[i].name

        #Updates runner's last race 
        for i in range(len(runners)):
            runners[i].last_race_time = runners[i].last_race_time = runners_time[i]
            runners[i].last_race_type = "200m"

        #Updates runners fastest time if applicable
        for i in range(len(runners)):
            
            if runners_time[i] < runners[i].fastest_200m:
                runners[i].fastest_200m = runners_time[i]

        print(f"200m: {len(runners)} runners")
        print("------------------------------")
        
        for i in range(len(runners)):

            print(f"Lane {i+1}: {runners[i].name} ran {runners[i].last_race_time}. OVR: {runners[i].overall_200m()}")

        print(f"The winner is {winner} with a time of {winning_time}")

        for i in range(len(runners)):
            runners[i].stamina -= 10

            Tracksim.sort_race(runners_time, runners)

    def four_hundred_meters_race(runners):
        
        runners_time = []
        winning_time = 60.00
        winner = None

        #Adds times to runners_time list
        for i in runners:
            runners_time.append(float(f"{Tracksim.four_hundred_meters(i):.2f}"))

        #Finds fastest time and sets that to winning time and assigns the winner
        for i in range(len(runners_time)):
            
            if (runners_time[i] < winning_time):
                
                winning_time = runners_time[i]
                winner = runners[i].name

        #Updates runner's last race 
        for i in range(len(runners)):
            runners[i].last_race_time = runners[i].last_race_time = runners_time[i]
            runners[i].last_race_type = "400m"

        #Updates runners fastest time if applicable
        for i in range(len(runners)):
            
            if runners_time[i] < runners[i].fastest_400m:
                runners[i].fastest_400m = runners_time[i]

        print(f"400m: {len(runners)} runners")
        print("------------------------------")
        
        for i in range(len(runners)):

            print(f"Lane {i+1}: {runners[i].name} ran {runners[i].last_race_time}. OVR: {runners[i].overall_400m()}")

        print(f"The winner is {winner} with a time of {winning_time}")

        for i in range(len(runners)):
            runners[i].stamina -= 10

            Tracksim.sort_race(runners_time, runners)

def game_loop():

    run_program = True
    attribute_points = 150

    while run_program:

        print("Create your player!")
        name = input("Input a name: ")

        #User age input, make sure input is a number and is between 18-40
        while True:
            try:
                age = int(input("Input an age between 18 and 40: "))
                if 18 <= age <= 40:
                    break  # Break out of the loop if input is an integer within the range
                else:
                    print("Age must be between 18 and 40. Please try again.")
            except ValueError:
                print("Input is not a valid integer. Please try again.")
            
        print("You have a maximum of 150 attribute points. Attributes scale 0 to 100. You have 6 attributes. Acceleration, Endurance, Form, Mental, Speed, Start")

        #Prompts user to input set their attribute points. Loops until all attribute points are used
        while attribute_points > 0:

            #Sets acceleration attribute based on user input
            acceleration = None
            while acceleration is None or acceleration < 0 or acceleration > min(100, attribute_points):

                try:
                    acceleration = int(input(f"Input your acceleration(0-100). You have {attribute_points} attribute point(s) remaining: "))

                except ValueError:
                    print("Input is not a valid number. Please try again:")

                if acceleration is not None and (acceleration < 0 or acceleration > min(100, attribute_points)):
                    print(f"That number is not between 0 and {min(100, attribute_points)}. Please try again.")

            attribute_points -= acceleration
            print(f"Your acceleration is {acceleration}. You have {attribute_points} attribute point(s) remaining and 5 attributes left.")

            #Checks if all attribute points are used. If so the rest of the attributes are set to 0 and the loop is broken
            if attribute_points <= 0:
                endurance = form = mental = speed = start = 0
                break

            #Sets endurance attribute based on user input
            endurance = None
            while endurance is None or endurance < 0 or endurance > min(100, attribute_points):

                try:
                    endurance = int(input(f"Input your endurance(0-100). You have {attribute_points} attribute point(s) remaining: "))

                except ValueError:
                    print("Input is not a valid number. Please try again: ")

                if endurance is not None and (endurance < 0 or endurance > min(100, attribute_points)):
                    print(f"That number is not between 0 and {min(100, attribute_points)}. Please try again.")

            attribute_points -= endurance
            print(f"Your endurance is {endurance}. You have {attribute_points} attribute point(s) remaining and 4 attributes left")

            #Checks if all attribute points are used. If so the rest of the attributes are set to 0 and the loop is broken
            if attribute_points <= 0:
                form = mental = speed = start = 0
                break

            #Sets form attribute based on user input
            form = None
            while form is None or form < 0 or form > min(100, attribute_points):

                try:
                    form = int(input(f"Input your form(0-100). You have {attribute_points} attribute point(s) remaining: "))

                except ValueError:
                    print("Input is not a valid number. Please try again: ")

                if form is not None and (form < 0 or form > min(100, attribute_points)):
                    print(f"That number is not between 0 and {min(100, attribute_points)}. Please try again.")

            attribute_points -= form
            print(f"Your form is {form}. You have {attribute_points} attribute point(s) remaining and 3 attributes left")

            #Checks if all attribute points are used. If so the rest of the attributes are set to 0 and the loop is broken
            if attribute_points <= 0:
                mental = speed = start = 0
                break

            #Sets mental attribute based on user input
            mental = None
            while mental is None or mental < 0 or mental > min(100, attribute_points):

                try:
                    mental = int(input(f"Input your mental(0-100). You have {attribute_points} attribute point(s) remaining: "))

                except ValueError:
                    print("Input is not a valid number. Please try again: ")

                if mental is not None and (mental < 0 or mental > min(100, attribute_points)):
                    print(f"That number is not between 0 and {min(100, attribute_points)}. Please try again.")

            attribute_points -= mental
            print(f"Your mental is {mental}. You have {attribute_points} attribute point(s) remaining and 2 attributes left")

            #Checks if all attribute points are used. If so the rest of the attributes are set to 0 and the loop is broken
            if attribute_points <= 0:
                speed = start = 0
                break
            
            #Sets speed attribute based on user input
            speed = None
            while speed is None or speed < 0 or speed > min(100, attribute_points):

                try:
                    speed = int(input(f"Input your speed(0-100). You have {attribute_points} attribute point(s) remaining. Any unused points will be used in the last category: "))

                except ValueError:
                    print("Input is not a valid number. Please try again: ")

                if speed is not None and (speed < 0 or speed > min(100, attribute_points)):
                    print(f"That number is not between 0 and min(100, attribute_points). Please try again.")

            attribute_points -= speed
            print(f"Your speed is {speed}. You have {attribute_points} attribute point(s) remaining and 1 attribute left.")

            #Checks if all attribute points are used. If so the rest of the attributes are set to 0 and the loop is broken
            if attribute_points <= 0:
                start = 0
                break

            start = None
            while start is None or start < 0 or start > min(100, attribute_points):

                try:
                    start = int(input(f"Input your start(0-100). You have {attribute_points} attribute point(s) remaining: "))

                except ValueError:
                    print("Input is not a valid number. Please try again: ")

                if mental is not None and (start < 0 or start > min(100, attribute_points)):
                    print(f"That number is not between 0 and {min(100, attribute_points)}. Please try again.")

            attribute_points -= start
            print(f"Your start is {start}. You have {attribute_points} attribute point(s) remaining")

            #Checks if all attribute points are used. If so the rest of the attributes are set to 0 and the loop is broken
            if attribute_points <= 0:
                speed = start = 0
                break

        user = Player(name, age, acceleration, endurance, form, mental, speed, start)
        #testing results for maxed player
        #user.acceleration = user.endurance = user.form = user.mental = user.speed = user.start = 100
        players = []
        players.append(user)
        Players.generate_random_characters(7, players)

        print(f"This is your player: {user}" )
        print("Let the game begin!")
        main_game = True
        while main_game:

            print("Would you like to compete? If so press 1")
            print("Would you like to practice? If so press 2")
            print("Would you like to rest? If so press 3")

            choice = int(input())

            if choice == 1:

                #intializing list to be filled with runners
                runners = []

                #Filling runners with players from players list
                for i in players:
                    runners.append(i)

                print("What race would you like to run?")
                print("1: 100m")
                print("2: 200m")
                print("3: 400m")

                choice = int(input())

                if choice == 1:

                    Tracksim.one_hundred_meters_race(runners)

                    print(f"You placed {user.place} with a time of {user.last_race_time}")

                    print(user)

                if choice == 2:

                    Tracksim.two_hundred_meters_race(runners)

                    print(f"You placed {user.place} with a time of {user.last_race_time}")

                    print(user)

                if choice == 3:

                    Tracksim.four_hundred_meters_race(runners)

                    print(f"You placed {user.place} with a time of {user.last_race_time}")

                    print(user)

                run_program = False
                main_game = False

        run_program = False

game_loop()