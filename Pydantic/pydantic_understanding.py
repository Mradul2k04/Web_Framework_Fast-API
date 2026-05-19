from pydantic import  BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patien',description="Give name of th patient in less than 50 char",examples=['Nitish','amit'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int
    weight:float=Field(gt=0,lt=120)
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print("inserted")
    
patient_info={'name':'mradul','email':'abc@gmail.com','linkedin_url':'http://linkedin.com','age':'30','weight':75.6,'married':True,'allergies':['Pollen','dust'],'contact_details':{"phone":"2551349294"}}

patient1=Patient(**patient_info)
insert_patient_data(patient1)
