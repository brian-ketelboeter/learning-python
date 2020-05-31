counting_number = 0
prompt = "Tell me how long you want me to run."
prompt += "\nGive me an integer value greater than 1: "
number = input(prompt)
while counting_number <= int(number):
    counting_number += 1

    if counting_number % 2 == 0:
        continue
    print(counting_number)
    
prompt = "Tell me something and I will repeat it back."
prompt += "\nWhen you wish for me to quite enter 'quit': "

active  = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message) 
