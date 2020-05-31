odds = []
cubes = []
for m in range(1,21,2):
    odds.append(m)
print(odds)

odds = list(range(3,30,3))
print(odds)
for n in range(1,20):
    cube = n**3
    cubes.append(cube)
print(cubes)

cubes = [n**3 for n in range(1,30)]
print(cubes)


