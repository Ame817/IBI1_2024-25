import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:/1-ZJEzrz/IBI/IBI1_2024-25/IBI1_2024-25/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

first_10_years=dalys_data.iloc[0:10,2]
print(first_10_years)
print(first_10_years[9],'was the 10th year with DALYs data recorded in Afghanistan.')
#1999 was the 10th year with DALYs data recorded in Afghanistan.

year1990=dalys_data.loc[dalys_data.Year==1990,['Year','Entity','DALYs']]
print(year1990)

uk_DALYs=dalys_data.loc[dalys_data.Entity=="United Kingdom", "DALYs"]
france_DALYs=dalys_data.loc[dalys_data.Entity=="France", "DALYs"]
def mean(list):
    float_list=[float(x) for x in list]
    mean=sum(float_list)/len(float_list)
    return(mean)
    
mean_uk=mean(uk_DALYs)
mean_france=mean(france_DALYs)
print('The mean DALYs in the UK was',mean_uk,', The mean DALYs in the France was',mean_france)
if mean_uk > mean_france:
    print('The mean DALYs in the UK was higher than the mean DALYs in the France')
elif mean_uk < mean_france:
    print('The mean DALYs in the UK was lower than the mean DALYs in the France')
else:
    print('The mean DALYs in the UK was equal to the mean DALYs in the France')

#The mean DALYs in the UK was greater than the mean DALYs in the France.

uk=dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'bo')
plt.xlabel('Year')
plt.ylabel('DALYs data in uk')
plt.title('The change of DALYs data in uk')
#'b' or 'r'-colors; 'o' or +'-shape of the points
plt.xticks(uk.Year,rotation=-45)
plt.show()

dalys_650000=dalys_data.loc[dalys_data.DALYs>=650000,"Entity"]
list_650000=dalys_650000.tolist()
year_650000=dalys_data.loc[dalys_data.DALYs>=650000,"Year"].tolist()
print(list_650000, 'have recorded a DALYs greater than 650,000 in a single year. Year:',year_650000)
# Rwanda have recorded a DALYs greater than 650,000 in a single year (1994).
