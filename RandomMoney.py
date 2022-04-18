# farz konid yek otagh darim ke tosh 50 nafar adam hastand.va ha kodom az in adamha 100 dolar pol darand. man miram to va yek beshkan mizanam,
# vaghti man beshkan mizanam har adami 1$ be ye adame random mideh, beshkan badi ro ke mizanam har adami 1$ be ye adamae random dige mideh,...
# (dar vagh az in tarigh dareh pol jabeja mishe). bad az ye modat chi misheh? agar kasi polesh tamom shode boud, dige to bazi nist.
# pas man ba har beshkanam ye adami(dar vagh har kodom az on adamha) 1$ random be ye adam dige midan.

import random

random.seed()
# for i in range (1, 10):
#    print(random.randrange(0, 2))

# return 0

people = []
for i in range(0, 50):
    people.append(100)

for beshkan in range(0, 100):
    for person1 in range(0, 50):

        person2 = random.randrange(0, 50)
        while people[person2] == 0:
            person2 = random.randrange(0, 50)

        if people[person1] != 0:
            # print(person1 ,person2)
            people[person1] = people[person1] - 1
            people[person2] = people[person2] + 1

print(people)
