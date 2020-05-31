places = ['regina', 'madison', 'chicago', 'siberia', 'yellow knife', 'point barrow']
print(places)

print(sorted(places))
print(places)

places.sort()
print(places)

places.sort(reverse = True)
print(places)

many_Places = len(places)
print("I want to visit", many_Places, "in my life!")

places.append('milwaukee')
print(places)

print("Now I wish to visit", len(places),"places!")
