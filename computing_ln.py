import math

for n in range(3, 10):
    m = math.log(n)
    value = 1/(n*m)
    number = n**-(1.1)
    difference = number - value
    print(str(n)+", " +str(value)+", " +str(number)+", " +str(difference)) 
