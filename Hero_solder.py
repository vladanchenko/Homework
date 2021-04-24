import random
class Solder:
    def __init__(self,team, id):
        self.team = team
        self.id = id

    def follow_the_hero(self, hero):
        print("Solder", self.id, "follow the Hero", hero.id)

class Hero(Solder):
    def __init__(self, team, id, lvl):
        Solder.__init__(self, team, id)
        self.lvl = lvl

    def growth_level(self):
        self.lvl += 1
        print("Hero", self.id, "up LVL")

hero1 = Hero(1, 1, 0)
hero2 = Hero(2, 2, 0)

list_for_solder1 = []
list_for_solder2 = []

n = 0
while n < 10:
    s = Solder(random.randint(1, 2) , n+1)
    n += 1
    if s.team == 1:
        list_for_solder1.append(s)
    elif s.team == 2:
        list_for_solder2.append(s)

print("Emount of solders for Hero", hero1.id, "is", len(list_for_solder1),
      "\nEmount of solders for Hero", hero2.id, "is", len(list_for_solder2))

if len(list_for_solder1) >= len(list_for_solder2):
    hero1.growth_level()
    solder = random.choice(list_for_solder1)
    solder.follow_the_hero(hero1)
    print("Hero ID: ",hero1.id,", Solder ID: ", solder.id)
if len(list_for_solder1) <= len(list_for_solder2):
    hero2.growth_level()
    solder = random.choice(list_for_solder2)
    solder.follow_the_hero(hero2)
    print("Hero ID: ", hero2.id, ", Solder ID: ", solder.id)