import random
import numpy as np
#need to add xp for races, sort by place, mental should increase if in top 3, stay the same if in 4,5 and decrease if in bottom 3, +5 +3 +1 0 0 -1 -3 -5. add else statements for invalid options. make rest or train excecute for sucessful rests
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
    
    def set_attribute(attribute_name, attribute_points):
        attribute = None

        while attribute is None or attribute < 0 or attribute > min(100, attribute_points):
            try:
                
                attribute = int(input(f"Input your {attribute_name}(0-100). You have {attribute_points} attribute point(s) remaining: "))
            except ValueError:
                print("Input is not a valid number. Please try again: ")
            if attribute is not None and (attribute < 0 or attribute > min(100, attribute_points)):
                print(f"That number is not between 0 and {min(100, attribute_points)}. Please try again.")
        return attribute
    
    def set_acceleration(self, value):
        self.acceleration = max(0, min(value, 100))

    def set_endurance(self, value):
        self.endurance = max(0, min(value, 100))

    def set_form(self, value):
        self.form = max(0, min(value, 100))

    def set_mental(self, value):
        self.mental = max(0, min(value, 100))

    def set_speed(self, value):
        self.speed = max(0, min(value, 100))

    def set_stamina(self, value):
        self.stamina = max(0, min(value, 100))

    def set_start(self, value):
        self.start = max(0, min(value, 100))

class Players:

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

    def random_train(player):

        training_options = [Players._100_practice, Players._200_practice, Players._400_practice, Players.acceleration_practice, Players.endurance_practice, Players.form_practice, Players.mental_practice, Players.speed_practice, Players.start_practice]

        random_function = random.choice(training_options)

        return random_function(player)
    
    def rest_or_train(player):
        
        options = [Players.random_train, Players.rest]

        random_function = random.choice(options)
        if random_function == Players.rest:
            return f"{player.name}: {random_function(player)}"

        return random_function(player)

    def rest(player):

        if player.stamina >= 100:
           return "You've maxed your stamina!\n"

        else:
            #sublist = players[1:8]
            #for i in sublist:
                #print(Players.rest_or_train(i))

            stamina_gained = random.randint(1,10)
            player.set_stamina(player.stamina + stamina_gained)
            return f"You've rested and gained {stamina_gained} stamina\nYour stamina is now {player.stamina}.\n"
        
    
    def _100_practice(player):

        #Random amount of xp
        xp = random.randint(1,5)
        xp2 = random.randint(1,3)
        xp3 = random.randint(1,2)
        stamina_loss = 10

        #Adding random xp
        player.set_acceleration(player.acceleration + xp)
        player.set_speed(player.speed + xp2)
        player.set_start(player.start + xp3)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved acceleration by {xp}, speed by {xp2}, and stamina by {xp3}. You used {stamina_loss} stamina.\n"

    def _200_practice(player):

        #Random amount of xp
        xp = random.randint(1,5)
        xp2 = random.randint(1,3)
        xp3= random.randint(1,2)
        stamina_loss = 10

        #Adding random xp and decreasing stamina
    
        player.set_speed(player.speed + xp)
        player.set_acceleration(player.acceleration + xp2)
        player.set_endurance(player.endurance + xp3)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved speed by {xp}, acceleration by {xp2}, and endurance by {xp3}. You used {stamina_loss} stamina.\n"

    def _400_practice(player):

        #Random amount of xp
        xp = random.randint(1,5)
        xp2 = random.randint(1,3)
        xp3= random.randint(1,2)
        stamina_loss = 10

        #Adding random xp and decreasing stamina
    
        player.set_endurance(player.endurance + xp)
        player.set_form(player.form + xp2)
        player.set_speed(player.speed + xp3)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved endurance by {xp}, form by {xp2}, and speed by {xp3}. You used {stamina_loss} stamina.\n"

    def acceleration_practice(player):

        xp = random.randint(5,10)
        stamina_loss = 5

        player.set_acceleration(player.acceleration + xp)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved acceleration by {xp}. You used {stamina_loss} stamina.\n"

    def endurance_practice(player):

        xp = random.randint(5,10)
        stamina_loss = 5

        player.set_endurance(player.endurance + xp)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved endurance by {xp}. You used {stamina_loss} stamina.\n"

    def form_practice(player):

        xp = random.randint(5,10)
        stamina_loss = 5

        player.set_form(player.form + xp)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved form by {xp}. You used {stamina_loss} stamina.\n"

    def mental_practice(player):

        xp = random.randint(5,10)
        stamina_loss = 5

        player.set_mental(player.mental + xp)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved mental by {xp}. You used {stamina_loss} stamina.\n"

    def speed_practice(player):

        xp = random.randint(5,10)
        stamina_loss = 5

        player.set_speed(player.speed + xp)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved speed by {xp}. You used {stamina_loss} stamina.\n"

    def start_practice(player):

        xp = random.randint(5,10)
        stamina_loss = 5

        player.set_start(player.start + xp)
        player.set_stamina(player.stamina - stamina_loss)

        return f"{player.name} improved start by {xp}. You used {stamina_loss} stamina.\n"

class Tracksim():

    def sort_race(runners_time, runners):

        runners_time.sort()

        for i in runners:
            for j in range(len(runners_time)):
                
                if i.last_race_time == runners_time[j]:
                    i.place = j + 1

    def one_hundred_meters(runner):
        
        mean100m = 10.7459527863
        sd100m = 0.133776557
        max_time = 8.00  # Maximum overall performance time
        overall = runner.overall_100m()

        # Adjusting mean and standard deviation based on overall performance
        mean = mean100m - (overall - 50) * (mean100m - max_time) / 50
        
        # Generating random time within the adjusted mean and standard deviation
        time = np.random.normal(mean, sd100m)
        
        return time

    def two_hundred_meters(runner):

        mean200m = 21.52218721
        sd200m = 0.160942679
        max_time = 15.80
        overall = runner.overall_200m()

        # Adjusting mean and standard deviation based on overall performance
        mean = mean200m - (overall - 50) * (mean200m - max_time) / 50
        
        # Generating random time within the adjusted mean and standard deviation
        time = np.random.normal(mean, sd200m)
        
        return time
    
    def four_hundred_meters(runner):

        mean400m = 44.8896305
        sd400m = 0.3135084355
        max_time = 35.60
        overall = runner.overall_400m()

        # Adjusting mean and standard deviation based on overall performance
        mean = mean400m - (overall - 50) * (mean400m - max_time) / 50
        
        # Generating random time within the adjusted mean and standard deviation
        time = np.random.normal(mean, sd400m)
        
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

        for i in runners:
            pass
            
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

        print("Create your player!\n")
        name = input("Input a name: \n")
        print()

        #User age input, make sure input is a number and is between 18-40
        while True:
            try:
                age = int(input("Input an age between 18 and 40: \n"))
                print()

                if 18 <= age <= 40:
                    break  # Break out of the loop if input is an integer within the range
                else:
                    print("Age must be between 18 and 40. Please try again.\n")
            except ValueError:
                print("Input is not a valid integer. Please try again.\n")
            
        #Prompts user to input set their attribute points. Loops until all attribute points are used
        while attribute_points > 0:

            print(f"You have a maximum of {attribute_points} attribute points. Attributes scale 0 to 100. You have 6 attributes. Acceleration, Endurance, Form, Mental, Speed, Start\n")
        
            acceleration = Player.set_attribute("acceleration", attribute_points)
            attribute_points -= acceleration
            print(f"Your acceleration is {acceleration}. You have {attribute_points} attribute point(s) remaining and 5 attributes left.\n")

            if attribute_points == 0:
                endurance = form = mental = speed = start = 0
                print("You've used all your attribute points\n")
                break
            
            endurance = Player.set_attribute("endurance", attribute_points)
            attribute_points -= endurance
            print(f"Your endurance is {endurance}. You have {attribute_points} attribute point(s) remaining and 4 attributes left.\n")

            if attribute_points == 0:
                form = mental = speed = start = 0
                print("You've used all your attribute points\n")
                break
            
            form = Player.set_attribute("form", attribute_points)
            attribute_points -= form
            print(f"Your form is {form}. You have {attribute_points} attribute point(s) remaining and 3 attributes left.\n")

            if attribute_points == 0:
                mental = speed = start = 0
                print("You've used all your attribute points\n")
                break
            
            mental = Player.set_attribute("mental", attribute_points)
            attribute_points -= mental
            print(f"Your mental is {mental}. You have {attribute_points} attribute point(s) remaining and 2 attributes left.\n")

            if attribute_points == 0:
                speed = start = 0
                print("You've used all your attribute points\n")
                break
            
            speed = Player.set_attribute("speed", attribute_points)
            attribute_points -= speed
            print(f"Your speed is {speed}. You have {attribute_points} attribute point(s) remaining and 1 attribute left.\n")

            if attribute_points == 0:
                start = 0
                print("You've used all your attribute points\n")
                break
            
            start = Player.set_attribute("start", attribute_points)
            attribute_points -= start
            print(f"Your start is {start}. You have {attribute_points} attribute point(s) remaining.\n")

            if attribute_points == 0:
                print("You've used all your attribute points\n")
                break

        user = Player(name, age, acceleration, endurance, form, mental, speed, start)
        #testing results for maxed player
        #user.acceleration = user.endurance = user.form = user.mental = user.speed = user.start = 100
        players = []
        players.append(user)
        Players.generate_random_characters(7, players)
        players[1].acceleration = players[1].endurance = players[1].form = players[1].mental = players[1].speed = players[1].start = 0
        players[4].acceleration = players[4].endurance = players[4].form = players[4].mental = players[4].speed = players[4].start = 45

        print(f"This is your player: {user}\n" )
        print("Let the game begin!\n")
        main_game = True
        while main_game:

            print("Would you like to compete? If so enter 1")
            print("Would you like to practice? If so enter 2")
            print("Would you like to rest? If so enter 3")
            print("Would you like to display your player? if so enter 4")
            print("Would you like to go back? If so enter 5")
            print("Would you like to exit? If so enter 6")
            print()

            choice = int(input())
            print()

            if choice == 1:

                #intializing list to be filled with runners
                runners = []

                #Filling runners with players from players list
                for i in players:
                    runners.append(i)

                while True:
                    
                    print("What race would you like to run?")
                    print("1: 100m")
                    print("2: 200m")
                    print("3: 400m")
                    print("4: Back")
                    print("5: Exit")
                    print()

                    choice = int(input())
                    print()

                    if choice == 1:

                        Tracksim.one_hundred_meters_race(runners)

                        print(f"You placed {user.place} with a time of {user.last_race_time}\n")
                        print(user)
                        print()

                    elif choice == 2:

                        Tracksim.two_hundred_meters_race(runners)

                        print(f"You placed {user.place} with a time of {user.last_race_time}\n")
                        print(user)
                        print()

                    elif choice == 3:

                        Tracksim.four_hundred_meters_race(runners)

                        print(f"You placed {user.place} with a time of {user.last_race_time}\n")
                        print(user)
                        print()

                    elif choice == 4:
                        print()
                        break

                    elif choice == 5:
                        run_program = False
                        main_game = False
                        break

            elif choice == 2:
                
                while True:

                    print("1:100m Practice(You gain a random amount of xp in acceleration, speed, and start)")
                    print("2:200m Practice(You gain a random amount of xp in acceleration, speed, and endurance)")
                    print("3:400m Practice(You gain a random amount of xp in endurance, form, and speed)")
                    print("4:Acceleration practice (You gain a random amount of xp ranging from 5-10)")
                    print("5:Endurance practice (You gain a random amount of xp ranging from 5-10)")
                    print("6:Form practice (You gain a random amount of xp ranging from 5-10)")
                    print("7:Mental practice (You gain a random amount of xp ranging from 5-10)")
                    print("8:Speed practice (You gain a random amount of xp ranging from 5-10)")
                    print("9:Start practice (You gain a random amount of xp ranging from 5-10)")
                    print("10: Back")
                    print("11: Exit Game")
                    print()

                    choice = int(input())
                    print()

                    if choice == 1:
                        print(Players._100_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 2:
                        print(Players._200_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 3:
                        print(Players._400_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 4:
                        print(Players.acceleration_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 5:
                        print(Players.endurance_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 6:
                        print(Players.form_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 7:
                        print(Players.mental_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 8:
                        print(Players.speed_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 9:
                        print(Players.start_practice(user))
                        sublist = players[1:8]
                        for i in sublist:
                            print(Players.rest_or_train(i))

                    elif choice == 10:
                        break

                    elif choice == 11:
                        run_program = False
                        main_game = False
                        break

            elif choice == 3:

                while True:

                    print(Players.rest(user))

                    print("Would you like to rest again?")
                    print("1: Yes")
                    print("2: Back")
                    print("3: Exit game")
                    print()

                    choice = int(input())

                    if choice == 1:
                        continue

                    elif choice == 2:
                        break

                    elif choice == 3:
                        run_program = False
                        main_game = False
                        break

            elif choice == 4:
                print(user)
                print()

            elif choice == 5:
                break
            
            elif choice == 6:
                run_program = False
                main_game = False

game_loop()