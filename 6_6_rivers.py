rivers = {'nile' : 'egypt', 'mississippi': 'united states',
          'danube' : 'germany',
          'voga' : 'russia', 'thames' : 'england', 'colorado' : 'united states',
          'amazon' : 'brazil', 'saskatchewan' : 'canada',
          'missouri' : 'united states', 'yellow' : 'china',
          'yang zhe' : 'china'
          }

for river,country in rivers.items():
    print(river.title() +" runs through " +country.title())

print('\n')
for river,country in rivers.items():
    if country == 'united states':
        print("Through the mother-land " +river.title() +" goeth!")
    else:
        print("The mother-land not " +river.title() +" goeth she.")

for country in set(rivers.values()):
    print(country)
