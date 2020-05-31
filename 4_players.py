players = ["ronaldo", "messi", "kane", "hazzard", "drogba",
           "abraham", 'james', 'pulisic', 'odoi','ampadu']
n = len(players)

print(players[5:])

for player in players[5:]:
    print(player.title() +" is a great Chelsea player")

print("Chelsea are the kings")

chelsea = players[5:]
print(chelsea)

great_players =  chelsea
print(great_players)

chelsea.append('kante')
great_players.append('hazzard')
print("Some of my favorite Chelsea players are")
print(chelsea)
print("\n A list of the greatest players in the world include:")
print(great_players)
