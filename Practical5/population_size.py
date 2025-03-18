#store the data in lists
uk_countries=[57.11,3.13,1.91,5.45]
china_provinces=[65.77,41.88,45.28,61.27,85.15]

print('The population in 2022 of each of the component countries in the UK:',uk_countries)
print('The population in 2022 of each of the provinces in China which corder Zhejiang province',china_provinces)

#print the lists
labels1=['England','Wales','Northern_Ireland','Scotland']
labels2=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']

#print the lists()
print('UK countries populations:')
for labels1, uk_countries in zip(labels1, uk_countries):
    print(f"{labels1}: {uk_countries}", 'millions')

print('China provinces populations:')
for labels2, china_provinces in zip(labels2, china_provinces):
    print(f"{labels2}: {china_provinces}",'millions')

import matplotlib.pyplot as plt
import numpy as np 

#the data, labels and colors for the first chart of the UK countries
uk_countries=[57.11,3.13,1.91,5.45]
x=np.array(uk_countries)
colors1=['#F18289','#FCD19C','#BED2C7','#CCDFE6']
labels1=['England','Wales','Northern_Ireland','Scotland']
#generate and show the first pie chart
plt.figure(1)
plt.pie(x,labels=labels1,colors=colors1)
plt.title('The population in 2022 of each of the component countries in the UK (millions)')

#the data, labels and colors for the first chart of the China provinces
china_provinces=[65.77,41.88,45.28,61.27,85.15]
y=np.array(china_provinces)
labels2=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']
colors2=['#FFE9A2','#E9D0BC','#BAC5C6','#9DA5C1','#676891']
#generate and show the first pie chart
plt.figure(2)
plt.pie(y,labels=labels2,colors=colors2)
plt.title('The population in 2022 of each of the provinces in China which corder Zhejiang province (millions)')
#show the pie chart
plt.show()

