import matplotlib.pyplot as plt
import numpy as np 

#------store the data in lists, then sort the data
#*the data and labels should be sorted together

#-store the data in lists
uk_countries=[57.11,3.13,1.91,5.45]
china_provinces=[65.77,41.88,45.28,61.27,85.15]
labels1=['England','Wales','Northern_Ireland','Scotland']
labels2=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']

#-combine the data and the labels together, then sort the combined lists; after that, separate them
#combine the two lists together
combineduk=list(zip(uk_countries,labels1))
combinedchina=list(zip(china_provinces,labels2))
#sort the combined lists
combineduk.sort()
combinedchina.sort()
#separate the sorted lists
uk_countries[:], labels1[:] = zip(*combineduk)
china_provinces[:], labels2[:] = zip(*combinedchina)


#print the sorted lists of populations in UK countries and China provinces
print('The population in 2022 of each of the component countries in the UK:',uk_countries)
print('The population in 2022 of each of the provinces in China which corder Zhejiang province',china_provinces)

#--------generate the pie chart
#put the two charts into one window
#The charts should include labels and percentage(in the pie chart) for each segment.

#the data, labels and colors for the first chart of the UK countries
x=np.array(uk_countries)
colors1=['#F18289','#FCD19C','#BED2C7','#CCDFE6'] 
#generatethe first pie chart
plt.figure(1)
plt.pie(x,labels=labels1,colors=colors1,autopct='%.1f%%') #"autopct='%.1f%%':show the percentage in the pie chart
plt.title('The population in 2022 of each of the component countries in the UK (millions)')

#the data, labels and colors for the first chart of the China provinces
y=np.array(china_provinces)
colors2=['#FFE9A2','#E9D0BC','#BAC5C6','#9DA5C1','#676891']
#generate the second pie chart
plt.figure(2)
plt.pie(y,labels=labels2,colors=colors2,autopct='%.1f%%')
plt.title('The population in 2022 of each of the provinces in China which corder Zhejiang province (millions)')

#---------print the percentage with their labels together, directly showing the informations to the user
#desired output format: someplace: xx millions

print('\n UK countries populations:')
for labels1, uk_countries in zip(labels1, uk_countries):
    print(f"{labels1}: {uk_countries}", 'millions')

print('\n China provinces populations:')
for labels2, china_provinces in zip(labels2, china_provinces):
    print(f"{labels2}: {china_provinces}",'millions')

#--warnings:this section should only put here
#if it is moved below "plt.show()",the program will hang, and the information won't be printed.
#if it is moved before pie charts generating codes, "uk_countries" and "china_provinces" cannot be successfully identified

#--------show the pie chart
plt.show()

