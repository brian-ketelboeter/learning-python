favorite_places = {'jill': ['cancun','toronto','san fransico'],
                   'robin': ['mozambique'],
                   'kim': ['mazatlan','sofia','moscow'],
                   'jeff': ['kiev','cologne'],
                   'franklin': ['mazomanie','black earth', 'bay of bisque'],
                   'boris': ['regina','vancouver'],
                   }
for person, places in favorite_places.items():
    if len(places) == 1:
        print(person.title() +"'s favorite place is:")
    else:
        print(person.title() +"'s favorite places are:")
    for place in places:
        print(place.title())
