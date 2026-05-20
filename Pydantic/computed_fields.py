from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print('BMI',patient.bmi)
    print("update")

patient_info={'name':'arjun','email':'arjun144@hdfc.com','age':'65','weight':82.5,'height':1.72,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'554545448','emergency':'626495256265'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)        