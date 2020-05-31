#I am inviting family members to a party
guest_list=['richard', 'glen', 'dorothy', 'merlin']

for k in range(0, len(guest_list)):
    print(guest_list[k].title() +" Ketelboeter is invited to my party!")

#of course, Richard is too busy
too_busy = guest_list.pop(0)
print("Well, it turns out "+too_busy.title() +" is too busy to make it!")
instead = 'carl'
#so I invited Carl instead
guest_list.append(instead)

for k in range(0, len(guest_list)):
    print(guest_list[k].title() +" Ketelboeter is invited to my party!")
    print("I have found a larger table!")

#Adding new guests
new_guests = ['leonard', 'margret', 'rose']
for k in range(1,len(new_guests)):
               guest_list.insert(k,new_guests[k])
guest_list.append(new_guests[0])

print(guest_list)

for k in range(0, len(guest_list)):
    print(guest_list[k].title() +" is welcome to my party!")

n = len(guest_list)-2
for k in range(0, n):
    not_invited = guest_list.pop()
    print("Ack! I can not invite " +not_invited.title() +" to my party!")

print(guest_list)

for k in range(0, len(guest_list)):
    not_invited = guest_list.pop()
    print("Ack! I can not invite " +not_invited.title() +" to my party!")

print(guest_list)
        

