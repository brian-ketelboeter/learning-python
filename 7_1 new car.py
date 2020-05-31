new_car = input("What kind of car would you like to buy? ")
prompt = "Are you sure you want to buy a " +new_car +"?"
prompt += "\nThose cars are junk."

print(prompt)
yugo = input("May I interest you in this fine Yugo? y or n ")

if yugo == 'y':
    print("Good I am happy to hear this.")
elif yugo == 'n':
    print("Maybe you did not hear my question correctly.")
else:
    print("please re-read the question.")
