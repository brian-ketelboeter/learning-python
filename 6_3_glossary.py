glossary = {
    'list' : 'ordered collection of objects',
    'set' : 'unordered collection of objects',
    'dictionary' : 'key-value pairs ordered',
    'for loop': 'a loop run over a certain collection of objects',
    'if command': 'logic command checks against condition runs if true',
    }
print(glossary)

glossary['function'] = 'block of code that only runs when called'
glossary['tuple'] = 'an ordered, unchangeable collection'
glossary['list'] = 'ordered, changeable collection'
glossary['set'] = 'collection which is unindexed, unordered and changeable.'
glossary['module'] = 'library of code functions which can be called for other programs'

print("\n")
for key, value in glossary.items():
    print(key)
    print(value)

