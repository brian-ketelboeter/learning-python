import math
#31 secant line values
values_upper =[.1,.01,.001,.0001, .00001]
values_lower =[-.1,-.01,-.001,-.0001, -.00001]

def function(x):
    y = .5*x
    return 10*math.e**y
for value in values_upper:
    top = function(value)- 10
    bottom = value 
    sec = top/bottom
    print(sec)
print('\n')
for value in values_lower:
    top = function(value)-10
    bottom = value 
    sec = top/bottom
    print(sec)
