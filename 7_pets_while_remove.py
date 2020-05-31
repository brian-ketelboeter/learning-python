#collection of routines using while loops and user inputs
#removing item from list
pets = ['cat', 'dog', 'horse', 'pig', 'cat', 'raccoon', 'cat', 'dog', 'rabbit']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#creating a dictionary of voters and responses
responses ={}
active_voter = True
clinton_counter = 0
trump_counter = 0
sanders_counter = 0
other_counter = 0
while active_voter:
#getting name of user
    name = input("Please give me your name: ")
    print("Hello " +name.title() +", we would like to know who you will vote for.")
#who voter is voting for?
    response = input("What candidate will you vote for? ")
    responses[name]= response
    if response == 'trump':
        trump_counter = trump_counter + 1
    elif response == 'sanders':
        sanders_counter = sanders_counter + 1
    elif response == 'clinton':
        clinton_counter = clinton_counter + 1
    else:
        other_counter = other_counter + 1
#any more voters?
    answer = input("Is there any other voters to respond to my poll? (yes/no) ")
    if answer == 'no':
        active_voter = False
#polling is complete. Print repsonses

for name,response in responses.items():
    print(name.title() +" is going to vote for " +response.title() +".")
print("\nClinton recieves ", clinton_counter)
print("\nSanders recieves ", sanders_counter)
print("\nTrump recieves  ", trump_counter)

#7.8 sandwich orders
sandwich_orders = ['ham and cheese', 'pastrami', 'vegetarian', 'cheese', 'blt',
                   'ham and cheese', 'club', 'pastrami', 'bbq chicken',
                   'teriaki chicken', 'pastrami',]
finished_orders = []

#7.9 adding a 'no pastrami' to sandwich orders
    
while sandwich_orders:
    order = sandwich_orders.pop(0)
    if order == 'pastrami':
        print("Sorry, we have no pastrami today.")
    else:
        finished_orders.append(order)
        print(order +" is up!")

print(finished_orders)

#7.10 dream vacation

users = ['jake', 'dorothy', 'daniel', 'danielle', 'toby']
prompt = "Where would you like to vacation this year? "
dream_vacation = {}

#gather vacation information
for user in users:
    vacation = input(user +prompt)
    dream_vacation[user] = vacation
print(dream_vacation)
