#a list of unconfirmed users.
#do they wish to use our program?
#while loop to check and move to one of two lists

unconfirmed_users =['tammy', 'ralph', 'constantien']
confirmed_users =[]
confirmed_non_user = []
prompt = " do you wish to use our program (y or n)?"

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    answer = input(current_user.title() +prompt)
    if answer == 'y':
        confirmed_users.append(current_user)
    if answer == 'n':
        confirmed_non_user.append(current_user)

print("\nThe users of our software include:") 
for user in confirmed_users:
    print('\t' +user)
