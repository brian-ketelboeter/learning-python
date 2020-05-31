users = []

if users:
    for user in users:
        if user == 'admin':
            print("Welcome " +user +". Would you like to make any changes to the game?")
        else:
            print("Welcome " +user.title() +" I hope you enjoy the game.")
else:
    print("I really need to get some people interested in this game!")
