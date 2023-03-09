from player import Player
from enemy import Enemy, Troll
tim = Player("Tim")
print("Player name: " + tim.name)
print("Player in in level: " + str(tim._level))
print("Player score: " + str(tim._score))
print("Player lives: " + str(tim.lives))
tim.lives -= 1
print("Player lives after hit: " + str(tim.lives))
"""
Můžu vypsat vše jen když si nechám vypsat tim prootže mám __str__ in my class
"""
print(tim)
tim.level = 5
print(tim)
tim.level += 30
print(tim)
tim.score += 500
print(tim)
tim.ammo += 40
print(tim)

random_monster = Enemy("Monster", 12, 2)

print(random_monster)
random_monster.take_damage(11)
print(random_monster)
random_monster.take_damage(8)
print(random_monster)
random_monster.take_damage(12)
print(random_monster)
random_monster.take_damage(12)
print(random_monster)

ugly_troll = Troll("Ugly troll")
print(ugly_troll)

more_ugly_trol = Troll("More Ugly Troll", 18, 3)
print(more_ugly_trol)