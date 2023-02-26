from player import Player

tim = Player("Tim")

print("Player name: " + tim.name)

print("Player in in level: " + str(tim.level))

print("Player score: " + str(tim.score))

print("Player lives: " + str(tim.lives))

tim.lives -= 1

print("Player lives after hit: " + str(tim.lives))


"""
Můžu vypsat vše jen když si nechám vypsat tim prootže mám __str__ in my class
"""
print(tim)
