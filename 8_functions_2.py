#second part on functions

def formated_full_name(first_name, last_name, middle_name =''):
    """return full name, properly formatted"""
    if middle_name:
        full_name = first_name +' '+middle_name+' '+last_name
    else:
        full_name = first_name +" "+last_name
    return full_name.title()
print(formated_full_name('john', 'lee', 'hooker'))

def build_person(first_name, last_name, age =''):
    person = {'first' : first_name, 'last': last_name}
    if age:
        person['age']=age
    return person
number = 0
persons = {}
more_people = True
while more_people:
    number = number + 1
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    age = input("please give me your age\n")
    people = input("Are there any more people there('y' or 'n')? ")
    persons[number] = build_person(first_name,last_name,age)
    if people == 'n':
        more_people = False
print(persons)

while True:
    print("Please give me your name.\n Enter 'q' at any time to quit.")
    first_name = input("What is your first name?\n")
    if first_name == 'q':
        break
    last_name = input("what is your last name?\n")
    if last_name == 'q':
        break
    print(formated_full_name(first_name,last_name))
#8.6 city and country
    
def city_country(city,country):
    place = [city.title(),country.title()]
    print(place)

#8.7 albums

def albums(artist,album_name,number_of_tracks =''):
    album ={'artist': artist, 'album name': album_name}
    if number_of_tracks:
        album['tracks']= number_of_tracks
    return album
groups = True
while groups:
    print("Please tell us about your favorite albums.\nType 'q' to quit")
    artist = input("Name of the artist?\n")
    if artist == 'q':
        break
    album = input("Name of the album?\n")
    if album == 'q':
        break
    albums(artist,album)

def greet_user(names):
    for name in names:
        print("Welcome, " +name.title())

names =[]
new_name = True
prompt = "Please provide us a list of all the people there.\n"
prompt +="Enter 'q' if there are no other people"
print(prompt)
while new_name:
    name = input("First name?\n")
    if name == 'q':
        break
    names.append(name)
greet_users(names)
