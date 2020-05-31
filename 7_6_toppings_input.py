toppings = []
prompt = "Are there any other toppings you would like (y or n)? "
prompty = "What topping would you like? "

moretopping = True

while moretopping == True:
    answer = input(prompt)
    if answer == 'y':
        moretopping = True
        topping = input(prompty)
        print("I will add " +topping +" to your order.")
        toppings.append(topping)
    else:
        moretopping = False

print("Your pizza's toppings are:")
for topping in toppings:
    print(topping)
