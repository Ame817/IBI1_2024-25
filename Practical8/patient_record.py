class patients(object):
    def __init__(self,name,age,last_admission_date,medical_history):
        self.name=name
        self.age=age
        self.last_admission_date=last_admission_date
        self.medical_history=medical_history
    def informations(self):
        print('Name:',self.name,'Age:',self.age,'Last admission date:',self.last_admission_date,'Medical history:',self.medical_history)
        
patient1=patients('Aris',25,'13/01/2025','The patient has type II diabetes.')
patient1.informations()