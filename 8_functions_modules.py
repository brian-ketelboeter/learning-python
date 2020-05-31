from eight_functions_3 import pizza_type as pt

toppings = []
more_topping = True
size = input("How big is your pizza (inches)?")

while more_topping == True:
    topping = input("Name one topping you would like on your pizza?")
    toppings.append(topping)
    answer = input("Any more toppings? ('y' or 'n')")
    if answer == 'n':
        more_topping = False
pt(int(size),toppings)
#passing to pizza_type list is causing problem.
#pizza_type reads toppings as one list (instead of numerous elements)
#example should call pizza_type(20, 'extra cheese', 'mushrooms'
#instead of pizza_type(20, toppings),
#toppings =['extra cheese', 'mushrooms']
#problem solved: removing '*' in function def sends list to function (instead of
#various number of argements). with *toppings, sending list of toppings counted
#as one variable as was treated as such.
