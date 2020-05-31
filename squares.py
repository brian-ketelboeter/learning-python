#wondering about checking conjecture every integer is the sum of two squeares
squares = []
adds = []
for value in range(1,20):
    square = value**2
    squares.append(square)

print(squares)

for value in squares:
    for k in squares:
        m = value + k
        adds.append(m)
    squares.remove(value)

new_adds = sorted(adds)
print(new_adds)


#some statistics
print(min(new_adds))
print(max(new_adds))
print(sum(new_adds))
