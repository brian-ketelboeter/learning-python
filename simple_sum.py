import math
#calculating a first 8 terms in series
s = 0
t = 0
for n in range(1,9):
    s = s + (n**2 +1)**(-1)
    print(str(n) +", " +str(s))

#calculating an arctan

Arctan = math.atan(8)
difference =  math.pi/2 -Arctan

print(str(Arctan))
print(str(difference))
print("\n")
for n in range(1,5):
    t = t + n*math.e**(-n**2)
    print(str(n) +", " +str(t))
print("\n")
remainder = math.e**(-16)/2
print(str(remainder))

print("\n")
M= 4*math.log(10)-math.log(5)

print(str(2*M))

print("\n")

for n in range(2,9):
    a = n**-1.1
    B = n*math.log(n)
    b = B**-1
    print(str(n) +", " +str(a) +", " +str(b))

print("\n")
x = math.pi /4
c = math.cos(x)
s = x**2
print(str(x) +", " +str(c) +", " +str(s))

x= 20
z = 40
y = 2* math.pi *(25*x**2-x**3/6 +40*z**2-2*z**3/3 -40*x**2+2*x**3/3)
print("\n" +"\t"+ str(y))

