def drug_dosage(weight,strength):
    if not 10.0<=weight<=100.0:
        print('ERROR:Sorry, the weight is out of normal range')
    if strength=='120mg/5ml':
        dosage=float(weight)*15/(120/5)
    elif strength=='250mg/5ml':
        dosage=float(weight)*15/(250/5)
    else:
        print('ERROR:Sorry, please choose the strength from 120mg/5ml and 250mg/5ml ')
    return(dosage)

print('The volume of paracetamol required is ',drug_dosage(12.0,'120mg/5ml'),'ml') #7.5ml