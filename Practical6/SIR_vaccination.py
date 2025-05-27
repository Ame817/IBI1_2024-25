#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#define the basic variables
N_total=10000 #the total population 
vaccinate_rate=0.5
beta=0.3 #infection probability of susceptible people
gamma=0.05 #recovering probability of infected people
#in each time point,random susceptible people will be infected. 
#the probability of making contact with an infected individual:
#multiplying beta by the proportion of infected people in the population
#=beta*number of infected people/population(N)
#random infected people will recover. probability=gamma

#start a loop, where one plot will be created in the loop of each vacciantion rate
vaccinate_rate=0
for vaccinate_rate in np.arange(0, 1.1, 0.1):
    N=int(N_total*(1-vaccinate_rate)) #the unvaccined population 

    #start from the initial status:1 infected, others are susceptible
    susceptible=N-1 
    infected=1
    recovered=0
    #these three variables are used to temporarily restore the number of susceptible/infected/recovered people

    #create the list to record the changing of infected population
    #start from the initial status,with only 1 number in the list
    #updated number in each loop will be appended into the list
    colors = cm.viridis(np.linspace(0, 1, 11))
    infected_list=[infected]
    n=1
    time=1000
    for n in range(1,time):
        if N!=0:
            delta=beta*infected/N
            #caculated by:probabily of infected after contacted(beta)*proportion of infected people

            #calculate the newly infected/recovered people:
            #1.randomly give value 0 or 1 to each people in susceptible/infected group 
            #in susceptible group, 1 represents 'newly infected',whose probability=delta
            #in infected group, 1 represents 'newly recovered', whose probability=gamma
            infecting=np.random.choice(range(2),susceptible,p=[1-delta,delta]) 
            #population of newly infected people=sum of the 1s in 'infecting' list
            recovering=np.random.choice(range(2),infected,p=[1-gamma,gamma])
            #population of newly recovered people=sum of the 1s in 'recovering' list

            #calculate the updated population of each group
            susceptible= susceptible-sum(infecting)
            infected = infected+sum(infecting)-sum(recovering)
            recovered += sum(recovering)

            #append the updated population number to the list
            infected_list.append(int(infected))
            x=list(range(1,time+1))
        else:
            infected_list.append(0)
    #create the plot for the line of this vaccination rate
    percentage_label = str(int(vaccinate_rate * 100)) + '%'   
    plt.plot(x,infected_list,label=percentage_label,color=colors[int(10*vaccinate_rate)])    

plt.xlabel("time")
plt.ylabel("number of people")
plt.legend()
plt.title('SIR model')
plt.show()

