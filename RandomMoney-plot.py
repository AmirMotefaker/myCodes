import random
random.seed()
#for i in range (1, 10):
#    print(random.randrange(0, 2))
    
#return 0

people = []
for i in range (0, 50):
    people.append(100)
    
for beshkan in range (0, 10000):
    for person1 in range (0, 50):
        
        person2 = random.randrange(0, 50)
        while people[person2] == 0:
            person2 = random.randrange(0, 50)
        
        if people[person1] != 0:
            #print(person1 ,person2)
            people[person1] = people[person1] - 1
            people[person2] = people[person2] + 1 
            
            
            
import matplotlib.pyplot as plt
%matplotlib inline 
# %matplotlib inline for graphical inotebook-jupyter

#people.sort()
plt.bar(range (0, 50), sorted(people, reverse=True))
