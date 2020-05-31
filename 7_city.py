prompt = "Please tell me all the cities you have visited"
prompt += "\n When you are finished, enter 'quit'  "
cities = []
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I also would love to visit " +city.title() +"!")
        cities.append(city)
print("So the cities you have visited are")
print(cities)
