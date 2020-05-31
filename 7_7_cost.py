age = input("Please tell me your age (in years): ")
nage = int(age)
if nage <=3:
    price = 'free'
elif 3< nage < 10:
    price = '$3'
elif 10 <= nage <= 15:
    price = '$7'
else:
    price = '$10'
if nage <= 3:
    print("Congrats! You get in " +price)
else:
    print("As you are " +age +" years old, you owe " +price)
