countries =['turkey', 'russia', 'australia', 'new zealand', 'papua new guinea', 'guinea',
            'guyanna', 'brazil', 'china', 'south korea', 'north korea', 'vietnam', 'burundii',
            'thailand', 'japan', 'taiwan', 'malasia', 'napaul', 'india', 'kazikstan', 'mongolia',
            'indonesia', 'philipines', 'east timor', 'maurisiaus', 'pakistan', 'afghanistan',
            'iran', 'iraq', 'saudi arabia', 'uae', 'oman', 'kuwait', 'cambodia', 'laos']
print(countries)
print(sorted(countries))
countries.sort(reverse = True)
print(countries)

countries.append('jordan')
print("A list containing Abdel's country")
print(countries)
print("I listed",len(countries),"countries. Not bad!")
countries.remove('taiwan')
print("China's list of countries")
print(countries)

nice_countries = countries[:10]
bad_countries = countries[11:-4]

for country in countries:
    if country in nice_countries:
        print(country +" is a nice country.")
    if country in bad_countries:
        print(country +" is a bad country!")
    elif country not in nice_countries and bad_countries:
        print("I am indifferent to " +country +"!")
print(nice_countries)
