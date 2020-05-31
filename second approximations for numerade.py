import math
#setting initial values
x = 0
y = 1
c = math.cos(x)
s = x**2
Min_list = []
#loop to find fixed point
for n in range(1000000):
    diff = math.cos(x) - x**2
    Min_list.append(abs(diff))
    stor_variable = x
    if diff > 0:
        x = x+y/2 
    elif diff < 0:
        x = x - y/2
    else:
        break
    y = stor_variable
print(min(Min_list))
        
