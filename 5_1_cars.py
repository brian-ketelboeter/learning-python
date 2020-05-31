car = 'audi'
person = 'tom'
animal = 'rabbit'
print("Is car== 'suburu'? I predict false")
print(car == 'suburu')

print("\nIs car == 'audi'? I predict true")
print(car == 'audi')

print("Is the animal != 'rabbit'? I predict 'False'")
print(animal != 'rabbit')

print("Is the person == 'Tom'? I predict 'False'")
print(person == 'Tom')
print(person.title()== 'Tom')
print(person.upper() =='TOM')

if animal != 'cat' or person != 'tom':
    print(animal +" is not a car or " +person +" not tom!")
    print(animal !='cat' or person != 'tom')

print("Is car == 'audi' and person == 'phillip'? I predict 'False'!")
print(car == 'audi' and person == 'phillip')

print("Is the car != 'audi'! I predict 'False'")
print(car != 'audi')

print("Is the car == 'audi' or the person != 'tom' or the animal != 'cow'. I predict 'False'")
print(car == 'audi' or person != 'tom' or animal != 'cow')

print("Is the car == 'audi' and the person != 'tom' or the animal != 'cow'. I predict 'False'")
print(car == 'audi' and person != 'tom' or animal != 'cow')
print(car == 'audi' and (person != 'tom' or animal != 'cow'))
print((car == 'audi' and person != 'tom') or animal != 'cow')

print("Is the car == 'audi' or the person != 'tom' and the animal != 'cow'. I predict 'False'")
print(car == 'audi' or person != 'tom' and animal != 'cow')
print(car == 'audi' or (person !='tom' and animal != 'cow'))

print("Is the car == 'audi' and the person != 'tom' and the animal != 'cow'. I predict 'False'")
print(car == 'audi' and person != 'tom' and animal != 'cow')
print(car =='audi' and (person != 'tom' and animal != 'cow'))
print("Is the person != 'tom'? I predict 'Falso'")
print(person != 'tom')

print("animal != rabbit' and person != 'tom' and car != 'audi'")
print((animal != 'rabbit' and person != 'tom') and car != 'audi')
print(animal != 'rabbit' and (person != 'tom' and car != 'audi'))
animals = ['rabbit', 'cat', 'dog', 'cow']

if animal in animals:
    print(animal +" is on the list")
else:
     print(animal +" is not on the list")
if animal in animals and person == 'dick':
    print(animal in animals)
if animal in animals and person != 'dick':
    print(person =='dick')
