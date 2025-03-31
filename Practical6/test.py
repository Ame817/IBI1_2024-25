#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#make array of all susceptibel population
population=np.zeros((100,100)) #This creates an “array of arrays”
#There are 100 rows and 100 columns, all of which are zero.

outbreak = np.random.choice(range(100), 2) #randomly pick 2 numbers
#representing the location of the first infected person
population[outbreak[0], outbreak[1]] = 1 
#change the status of picked person to 1(infected)

#an infected individual can infect any of its 8 neighbours with infection probability beta
#infected individual can recover with probability gamma
infected_location=np.where(population==1)
x=infected_location[0]
y=infected_location[1]

beta=0.3
gamma=0.05

for n in range(1,20):
    for a in range(0,100):
        for b in range(0,100):
            if population[a,b]==1:
                effect=np.random.choice(range(2),1,p=[1-gamma,gamma])
                if effect==1:
                    population[a,b]=2

            infected_location=np.where(population==1)
            x=infected_location[0]
            y=infected_location[1]
            for i, j in zip(x,y):
                if abs(a-i) + abs(b-j) <= 2:
                    if population[a,b]==0:
                        effect=np.random.choice(range(2),1,p=[1-beta,beta])
                        if effect==1:
                            population[a,b]=1

plt.figure(figsize=(6,5),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest') 
#Interpolation: a method of smoothing images.
#Fill in the gaps and make the image look more natural when enlarging or shrinking the image.
plt.show()
