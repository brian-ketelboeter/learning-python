#chapter 8 python crash course functions
def hello():
    """greets people"""
    print("Hello!")
hello()

def greetings(user):
    """greets person by name"""
    print("Hello " +user.title())
prompt = "Please give me your name? \n"

user = input(prompt)
greetings(user)

def summ(x):
    return x**4 + 4*x - 25

numbers = [35, 1, 0, 610]

for x in numbers:
    y = summ(x)
    print(y)
def display_message():
    """tells the world what we learn in this chapter"""
    print("Chapter 8 is about functions!")

def favorite_book(reader):
    print(reader.title() +"'s favorite book is 'Sound and the Fury'") 
display_message()
favorite_book(user)

for k in range(4):
    number = float(input("Give me a number "))
    y = summ(number)
    print(k, y, number)

def pet_func(pet_name, pet_type = "dog"):
    print("You have a " +pet_type +" named " +pet_name.title() +".")
pet = True
while pet == True:
    type = input("Please give us one type of pet you have ")
    name = input("Name one of your " +type +"s\n")
    pet_func(name,type)
    more_pets = input("Do you have any more pets?(y or n) ")
    if more_pets == 'n':
        pet = False
pet_func("Rawly")
#8.3 SHIRT NAME

def shirt_order(size="large",slogan= "I love python"):
    """prints out t-shirt order"""
    print("You would like a " +size +"-shirt with the slogan \n " +slogan +"!")
prompt = "I hear you would like a new shirt."
prompt += "What size would you like it in? "
prompty = "What slogan would you like on your shirt?"

size_in = input(prompt)
slogan_in = input(prompty)

shirt_order(size_in,slogan_in)

#8.5 CITY NAME

def city_name(city, country = 'United States'):
    print(city.title() +" is in " +country.title() +"!")
prompt = "Name a city \n"
prompty = "What country is that city in?\n"
city = input(prompt)
country = input(prompty)

city_name(city, country)
