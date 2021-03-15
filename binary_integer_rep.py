#statement = "a positive integer to find the binary represeentation of "

#num = int(input(statement))
negative_flag = False
result = ''
#checking positive value
if num < 0:
    negative_flag = True

if num == 0:
    result = '0'
elif negative_flag == False:
    while num > 0:
        k = num % 2
        num = int((num - k)/2)
        result = str(k) + result
        print(result)
        print(num)
else:
    num = abs(num)
    while num > 0:
        k = num % 2
        num = int((num - k)/2)
        result = str(k) + result
        print(result)
        print(num)

if negative_flag == True:
    print('-'+result)
else:
    print(result)


    
