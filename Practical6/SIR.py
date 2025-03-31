#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#define the basic variables
N=10000 #the total population 
beta=0.3 #infection probability of susceptible people
gamma=0.05 #recovering probability of infected people


#in each time point,random susceptible people will be infected. 
#the probability of making contact with an infected individual:
#multiplying beta by the proportion of infected people in the population
#=beta*number of infected people/population(N)
#random infected people will recover. probability=gamma

#start from the initial status:1 infected, others are susceptible
susceptible=N-1 
infected=1
recovered=0
#these three variables are used to temporarily restore the number of susceptible/infected/recovered people 

#create the lists to record the changing of the variables(number of people in each categories)
#start from the initial status,with only 1 number in each list.
#updated number in each loop will be appended into the lists
susceptible_list=[susceptible]
infected_list=[infected]
recovered_list=[recovered]

#start the loop
n=1 
time=1000 #number of loop
for n in range(1,time):
    delta=beta*infected/N #the probability of infected of susceptible people
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

    #append the updated population number to the lists
    susceptible_list.append(susceptible)
    infected_list.append(infected)
    recovered_list.append(recovered)
    n+=1

#create and show the plot
x=list(range(1,time+1))
plt.plot(x,susceptible_list,label='susceptible')
plt.plot(x,infected_list,label='infected')
plt.plot(x,recovered_list,label='recovered')
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend()
plt.title('SIR model')
plt.show()


