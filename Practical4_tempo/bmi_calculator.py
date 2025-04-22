#1.get the weight(in kg) and height(in m) from the user
weight=float(input("input your weight(kg)"))
height=float(input("input your height(m)"))
#2.calculate the bmi value by the fomula
bmi=(weight)/((height)**2)
#3.print the results
#bmi>30:obese
#18.5<=bmi<=30: in normal weight
#bmi<18.5:underweight
if bmi > 30:
	print("your bmi is ",bmi,"you are obese")
elif bmi<18.5:
	print("your bmi is ",bmi,"you are underweight")
else:
	print("your bmi is ",bmi,"you are in normal weight")
