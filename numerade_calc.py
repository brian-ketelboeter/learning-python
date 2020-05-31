import math
def function(x):
    return 24+12*x+x**2
times = [.1,.01,.001,.0001,.00001,.000001]

for time in times:
    y = function(time)
    print('\t' +str(y))
