available_toppings = ['extra cheese', 'mushrooms', 'green peppers',
                      'tomatoes', 'anchovies', 'pepperoni']
requested_toppings =['extra cheese', 'french fries', 'mushrooms',
                     'green peppers']

#if "mushrooms" in requested_toppings:
#    print("adding mushrooms")
#if "pepperoni" in requested_toppings:
#    print("adding pepperoni")
#if "extra cheese" in requested_toppings:
#    print("adding extra cheese")
#if "onions" in requested_toppings:
#    print("adding onions!")

#print("Your pizza is finished!")

if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            if topping == 'green peppers':
                print("Sorry we are out of " +topping +" currently!")
            else:
                print("Added "+topping +" to your pizza!")
        else:
            print("We do not serve "+topping +" here. Sorry.")
    print("Your pizza is done.")
           
else:
    print("Are you sure you want a plain pizza?")

#dictionaries

pizza = {'crust' : 'thick',
         'toppings' : ['mushrooms', 'onions'],
         'extra cheese': 'y'}
#summarize order

print("You ordered a " +pizza['crust'] +"-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" +topping)
           
               
         
             
    
