favorite_languages = {
    'toby': ['python','haskell','c#'],
    'annette' : ['c++'],
    'george' : ['ruby','java','javascript'],
    'leandra' : ['c++'],
    }
friends = ['george', 'annette']


print(favorite_languages)
for language in favorite_languages['toby']:
    print("Toby's favorite languages include:")
    print("\t" +language.title())

for name in favorite_languages:
          print(name.title() +" favorite languages are:")
          for language in favorite_languages[name]:
                print( "\t" +language.title())



for name in favorite_languages.keys():
    if name in friends:
        print("Hello " +name.title()
              +" good to see you. Your favorite language is "
              +favorite_languages[name])

    else:
        print(name.title() +" loves " +favorite_languages[name] +" the most.")
if 'erin' not in favorite_languages.keys():
    print("Erin what is your favorite language?")
favorite_languages['erin'] = 'fortran'
for name in sorted(favorite_languages.keys()):
    print(name.title() +": your favorite language is "
          +favorite_languages[name].title())

print("The following languages have been mentioned:")

for language in sorted(favorite_languages.values()):
    print(language.title())
print("\n")
for language in set(favorite_languages.values()):
    print(language)

print('\n')
people = ['kian', 'paul', 'marie', 'leandra', 'george']

print(people)

for person in people:
    if person not in set(favorite_languages.keys()):
        print("Hello! I need " +person.title() +"'s favorite language.")
    else:
        print("Thank you " +person.title() +" for taking our poll.")
