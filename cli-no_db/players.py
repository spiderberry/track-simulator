import random

class Players:

    def cpu_100_practice(player):

        xp = random.randint(1,5)
        xp2 = random.randint(1,3)
        xp3= random.randint(1,2)

        player.acceleration = player.acceleration + xp
        player.speed = player.speed + xp2
        player.start = player.start + xp3
        player.stamina = player.stamina - 10