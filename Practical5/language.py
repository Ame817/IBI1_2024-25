options={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5} #create the dictionary
print(options)
language=input("Please input a language:") #language is the modified variable here
#print the results
if language in options:
    print("The percentage of developers who use",language,"is" ,options[language],"%")
else:
    print("Sorry, data of this language is not found")
import matplotlib.pyplot as plt
import numpy as np

#generate the pie chart
x=np.array(["JavaScript","HTML","Python","SQL","TypeScript"]) 
y=np.array([62.3,52.9,51,51,38.5]) 
plt.bar(x,y,color="#2B6868") #create the bar plot with the color #2B6868
plt.ylabel('Percentage (%)')  # 添加y轴标签
plt.title('Developer Usage Percentage by Language')  # 添加标题
plt.show() #show the bar plot