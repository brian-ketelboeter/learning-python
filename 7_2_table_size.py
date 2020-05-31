prompt = "Welcome to Gherkins "
prompt +="my name is Henneritta."
print(prompt)
table_size = input("How many people in your party? ")

table_size = int(table_size)
if table_size < 8:
    print("We have a table right here.")
else:
    print("Please wait while I find you a table.")

number = table_size % 10

if number in range(0,5):
    print("I am happy to here this.")
elif number in range(5,7):
    print("this worrying.")
else:
    print("I can't deal with this!")
