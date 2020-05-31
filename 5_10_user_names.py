current_users = ['phillip', 'thomas', 'jake', 'carina', 'carrie', 'johnathan']

new_users = ['thomas', 'PHILLIP', 'pauline']

for user in new_users:
    if user.lower() in current_users:
        print("I am sorry, " +user +" is already taken. You must try a different user name.")
    else:
        print(user +" is an acceptable user name!")
