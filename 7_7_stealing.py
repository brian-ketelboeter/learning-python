prompt = "Do you have $1? (y or n) "
prompty = "Give it to me"
answers = ['y', 'yes', 'I do', 'ah huh', 'yep']
answer = input(prompt)

if answer not in answers:
    print("Screw you then.")
else:
    while answer in answers:
        print(prompty)
        answer = input(prompt)
    print("Fuck off mate. I'm down with you.")
