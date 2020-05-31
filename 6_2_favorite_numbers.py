import math
favorite_numbers = {
    'phillipe' : [15,21, 225],
    'toby' : [3277.15,math.pi],
    'anita' : [22/7,math.cos(math.pi /7)],
    'kelly' : [2],
    'doc' : [0,1],
    }
for person in favorite_numbers:
    if len(favorite_numbers[person])== 1:
        print(person.title() +"'s favorite number is:")
    else:
        print(person.title() +"'s favorite numbers are:")
    print(favorite_numbers[person])
    print('\n')
