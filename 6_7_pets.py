dog = {'owner': 'columbo',
       'type': 'dog',
       'name': 'dog',
       }
fifi = {'owner' : 'someone',
        'type': 'dog',
        'name': 'fifi'
        }
bobbi = {'owner' : 'a different person',
         'type': 'bird',
         'name': 'bobbi',
         }
sherm = {'owner' : 'that person',
         'type' : 'cat',
         'name': 'sherm',
         }
little_devil = {'owner' : 'dad',
                'type' : 'cat',
                'name' : 'little devil',
                }
silage = {'owner' : 'me',
          'type' : 'cow',
          'name': 'silage',
          }
apple = {'owner' : 'me',
         'type' : 'rabbit',
         'name': 'apple',
         }
pets = [dog,fifi, sherm, little_devil, silage, apple]

for pet in pets:
    for trait, fact in pet.items():
        print('\t' +trait +': '+fact)
    print('\n')
