import random, math

d6 = [1, 2, 3, 4, 5, 6]
d20 = [i for i in range(1,21)]

class Character:
    def __init__(self):
        self.strength = self.get_stat_from_die_roll()
        self.dexterity = self.get_stat_from_die_roll()
        self.constitution = self.get_stat_from_die_roll()
        self.intelligence = self.get_stat_from_die_roll()
        self.wisdom = self.get_stat_from_die_roll()
        self.charisma = self.get_stat_from_die_roll()
        self.hitpoints = 10 + modifier(self.constitution)

    def get_stat_from_die_roll(self):
        die_roll = random.choices(d6, k=4)
        die_roll.sort(reverse=True)
        random_stat = sum(die_roll[0:3])
        return random_stat

    def ability(self):
        return getattr(self, 'constitution')

def modifier(self):
    return math.floor((self - 10) / 2)

