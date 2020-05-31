import math
def position(time):
    return 8*time**2 - time**3/16
def avg_vel(time):
    return (position(time) - position(4))/(time - 4)

times = [4.1, 4.01, 4.001, 4.0001]

for time in times:
    print(str(time) +", " +str(position(time))+ ", " +str(avg_vel(time)))

def flu(time):
    return 5.3*(2*.093*time - .87)*math.e**(.093*time**2-.87*time)
