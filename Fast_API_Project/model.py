import json
import os

File_Path="Fast_API_Project\database.json"

def read_json():
    if not os.path.exists(File_Path):
        return []
    with open(File_Path,"r") as f:
        return json.load(f)
    
def write_json(data:list):
    with open(File_Path,"w") as f:
        json.dump(data,f,indent=4)  
        
        
new_todos=[
    
    {
        "id": 4,
        "name": "neha",
        "description": "Backend Developer"
        
    }    
]
existing_todo=read_json()
if existing_todo != []:
    new_todos.append(existing_todo)
write_json(new_todos)
print("Data successfully Added to json file") 
    