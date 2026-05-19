#Problem 1 - Type validation is not there in python
#Problem 2 - Data Validation

#Insert
def insert_patient_data(name:str,age:int):
    
    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError("Age can not br negative")
        else:
            print(name)
            print(age)
            print("insert into database")
    else:
        raise TypeError('Incorrect data type ')
    
    
insert_patient_data('mradul','30')    



#Update
def update_patient_data(name:str,age:int):
    
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("update")
    else:
        raise TypeError('Incorrect data type ')
    
    
insert_patient_data('mradul','30')    