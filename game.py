from player import Player

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
