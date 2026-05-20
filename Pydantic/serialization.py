from pydantic import BaseModel


class Address(BaseModel):
    city:str
    state:str
    pin:str
    
    
class Patient(BaseModel):
    
    name:str
    gender:str
    age:int
    address:Address
    
address_dict={'city':'Mathura','state':'Uttar Pradesh','pin':'281151'}

address1=Address(**address_dict)

patient_dict={'name':'karan','gender':'male','age':35,'address':address1}

patient1=Patient(**patient_dict)  

  
temp=patient1.model_dump(include=['name','gender'])
print(temp)
print(type(temp))

per=patient1.model_dump(exclude={'address':['state']})
print(per)
print(type(per))

json=patient1.model_dump_json()
print(json)
print(type(json))