options={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5} #create the dictionary
print(optionspy)
language='HTML' #language is the modified variable
if language in options:
    print(language, "'s percentage of developers who use this language is " ,options[language])
else:
    print("Sorry, data of this language is not found")
import matplotlib.pyplot as plt
import numpy as np

x=np.array(["JavaScript","HTML","Python","SQL","TypeScript"])
y=np.array([62.3,52.9,51,51,38.5])
plt.bar(x,y,color="#2B6868") #create the bar plot with the color #2B6868
plt.show() #show the bar plot

