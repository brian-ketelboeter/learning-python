def add_users(names):
    name = input("What is your name?\n")
    names.append(name)
    return names

def greet_users(names):
    for name in names:
        print("Hello " +name.title() +"! How are you?")

def user_status(names):
    active_users =[]
    inactive_users = []
    while names:
        name = names.pop()
        activity = input("Is " +name.title() +" an active user?('y' or 'n')")
        if activity == 'y':
            active_users.append(name)
        else:
            inactive_users.append(name)
    print("Our active users are:\n", active_users)
    greet_users(active_users)
    print("Users that are not active include:\n", inactive_users)

def show_magicians(names):
    for name in names:
        print(name.title() +" is a magician of first quality!")

def make_great(names) :
    new_names = []
    while names:
        name = names.pop()
        new_name = name.title() +" the Great"
        new_names.insert(0,new_name)
    return new_names

def pizza_type(size, toppings):
    """prints toppings"""
    if len(toppings) == 0:
        print("You no-ah want a pizza! Get outtta here")
    elif len(toppings) == 1:
        for topping in toppings:
            statement = "Making a 1-topping " +str(size)
            statement += " inch pizza with " +str(topping)
            print(statement)
    else:
        print("\nYour " +str(size) +"-inch pizza has the following toppings:")
        for topping in toppings:
            print("-" +topping)
        print("you-ah make your poppa a proud man!")

def build_user(first_name, last_name, **user_info):
    profile = {}
    profile['first name'] = first_name
    profile['last name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

def sandwich_order(bread_type, *toppings):
    print("On your "+str(bread_type) +" bread sandwich, you would like the following:\n")
    for topping in toppings:
        print(topping)

def make_car(make, model, **attributes):
    print("Your "+make.title() +" "+model.title() +" will have the following:")
    for key, value in attributes.items():
        print(key +" " +value)
        

    
