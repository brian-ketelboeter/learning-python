age = 11

if age <= 5:
    price = "free"
elif age <= 10:
    price = "5"
elif 65 <= age:
    price = "5"
else: 
    price = "10"

if price == "free":
    print("You eat free!")
else:
    print("it costs $" +str(price) +" to eat here!")
if age >= 65:
    print("You are old!")
