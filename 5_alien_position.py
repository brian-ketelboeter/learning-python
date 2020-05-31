alien_0 ={'x_position': 0, 'y_position': 25, 'speed': 'medium', 'color': 'green',
          'points': 5,
          }
alien_1 ={'x_position': 5, 'y_position': 10, 'speed': 'slow', 'color': 'yellow',
          'points': 10,
          }
alien_2= {'x_position': 0, 'y_position': 25, 'speed': 'fast', 'color': 'red',
          'points': 15,
          }
aliens = [alien_0, alien_1, alien_2]
alien_army_green=[]
#Using speed to change current position

for alien in aliens:
    print(alien)
    if alien['speed'] == 'slow':
        x_increment =1
    elif alien['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3
    alien['x_position'] =alien['x_position']+ x_increment
    print(alien)
for alien_number in range(30):
    new_alien ={'x_position': alien_number, 'y_position': 25, 'speed': 'medium',
                'color': 'green','points': 5,
                }
    alien_army_green.append(new_alien)

for alien in alien_army_green:
    if alien in alien_army_green[:5]:
        alien['color'] = 'yellow'
        alien['speed'] = 'slow'
        alien['points'] = 10
    if alien in alien_army_green[5:10]:
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print("\n")
print(alien_army_green)


    

