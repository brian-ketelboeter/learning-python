import math
#setting initial values
x = 0
y = 1
c = math.cos(x)
s = x**2
Min_dict = {}
#loop to find fixed point
for n in range(1000000):
    diff = math.cos(x) - x**2
    Min_dict.update({x:abs(diff)})
    stor_variable = x
    if diff > 0:
        x = x+y/2 
    elif diff < 0:
        x = x - y/2
    else:
        break
    y = stor_variable

#finding minimum value
temp = min(Min_dict.values()) 

#listing keys that correspond to minimum value
res = [key for key in Min_dict if Min_dict[key] == temp]

#printing minimum value and keys

print("The minimum value is: "+str(temp) + "found at: ")
print(res)
