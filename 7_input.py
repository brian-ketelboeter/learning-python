#a collection
counties = []
#gathering information about user
name = input("Please tell me your name: ")
prompt = "Giving us information about yourself will allow us to personalise"
prompt += "the messages your see and hear."
prompt += "\nPlease tell us something about yourself: "

message = input(prompt)

age = input("How old are you? ")
height = input("How tall are you, in inches: ")

#sharing the information
print("Hello "+name +". This is what I know about you:")
print(message)
print("your age is: " +age)

#some comments about the user
if int(age) > 18:
    print("You are an old person.")
else:
    print("You are too young")
if int(height) > 36:
    print("You may use the roller coaster.")
else:
    print("Maybe next year!")

number = input("Tell me a number and I will tell you if it is even or odd: ")

divider = int(number) % 2
if divider == 0:
    print("Your number is even.")
else:
    print("You have an odd number.")
        
