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

beta=0.3
gamma=0.05

for n in range(0,100):
    infected_location=np.where(population==1) #find the infected people
    x,y=infected_location
    for i in range(len(x)):  #i:infected people
        a,b = x[i],y[i]  #for the location of each infected people 
        #randomly decide whether the people will recover with probability=gamma
        effect=np.random.choice(range(2),1,p=[1-gamma,gamma]) 
        if effect==1: 
            population[a,b]=2 #if random number effect=1, change the status of this people to recovered

        
        for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]: #the relative position of 8 people around
            na,nb=a+dx,b+dy #find the 8 people next to each infected people (location:[na,nb])
            if 0<=na<=99 and 0<=nb<=99:
                if population[na,nb]==0:
                    effect=np.random.choice(range(2),1,p=[1-beta,beta])
                    #randomly decide whether the people will be infected with probability=beta
                    if effect==1:
                        population[na,nb]=1 #if random number effect=1, change the status of this people to infected
    #plot the figure of the number of loops=1,25,50,75,100
    if n==0 or n ==24 or n==49 or n==74 or n==99: 
        plt.figure(figsize=(6,5),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')   
        plt.title(f'2D SIR model after {n+1} times of propagation')              

#Interpolation: a method of smoothing images.
#Fill in the gaps and make the image look more natural when enlarging or shrinking the image.
plt.show()
