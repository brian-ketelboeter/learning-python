cities = {'kiev' :{'city name': 'kiev',
                 'country': 'ukrain',
                 'population': '2,875,000',
                 },
          'moscow' :{'city name': 'moscow',
                 'country': 'russia',
                 'population': '12.5 million',
                 },
          'new_york' :{'city name': 'new york',
                 'country': 'united states',
                 'population': '8,397,000',
                 },
          'toronto' :{'city name': 'toronto',
                 'country': 'canada',
                 'population': '2,954,000',
                 },
          'mexico' :{'city name': 'mexico',
                 'country': 'mexico',
                 'population': '8,850,000',
                 },
          'edinburgh' :{'city name': 'edinburgh',
                 'country': 'scotland',
                 'population': '580,000',
                 },
          }
capital_cities =['kiev','moscow', 'mexico', 'edinburgh']
for city in cities:
    if city['city name'] in capital_cities:
        city['capital city'] = 'y'
    else:
        city['capital city'] = 'n'
    for trait, fact in city:
        print(trait +": " +fact)
    
          
