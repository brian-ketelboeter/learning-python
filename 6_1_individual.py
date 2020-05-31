remus = {
    'first name': 'remus',
    'last name': 'floricel',
    'home country' : 'romania',
    'current country of residence' : 'canada',
    'current city of residence' : 'regina',
    'spouse' : 'cristina',
    'children' : 'theobald',
    'job': 'mathematician',
    'work place' : 'university of regina',
    }

joey = {
    'first name': 'johanna',
    'last name': 'hislop',
    'home country' : 'united states',
    'current country of residence' : 'united states',
    'current city of residence' : 'duluth',
    'spouse' : 'bill',
    'children' : 'two',
    'job': 'computer programmer',
    'work place' : 'ibm',
    }
alex = {
    'first name': 'alexander',
    'last name': 'maizlish',
    'home country' : 'ukraine',
    'current country of residence' : 'canada',
    'current city of residence' : 'toronto',
    'spouse' : 'unknown',
    'children' : 'one',
    'job': 'head mathematician',
    'work place' : 'wgames',
    }
ian = {'first name': 'ian',
       'last name': 'macausland-berg',
       'home country': 'canada',
       'current country of residence': 'canada',
       'current city of residence': 'regina',
       'spouse': 'unknown',
       'children': 'two',
       'job': 'psycologist',
       'work place': 'university of regina',
       }
peoples =[remus, joey,alex]
peoples.append(ian)
for person in peoples:
    print(person)
    for trait , fact in person.items():
        print('\t' +trait +': ' +fact)
