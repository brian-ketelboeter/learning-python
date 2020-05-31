users = {'bketelbo':{'first name': 'brian', 'last name': 'ketelboeter',
                     'location': 'regina',},
         'jhyslop':{'first name': 'johanna', 'last name': 'hyslop',
                    'location': 'duluth'},
         'ens':{'first name': 'eric', 'last name': 'ens',
                'location': 'toronto'},
         }
for user, user_info in users.items():
   full_name = user_info['first name'] +" " +user_info['last name']
   print("\t User name: " +user)
   print("\t Name: " +full_name.title())

