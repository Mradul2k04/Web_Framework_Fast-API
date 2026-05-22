from fastapi import HTTPException,APIRouter
from pydantic import BaseModel



router=APIRouter()

class ToDoCreate(BaseModel):
   
    name:str
    description:str
    
class ToDoResponse(ToDoCreate)  :
     id:int
    
    
todos=[] 
   
@router.get('/')
def show_Todos():
    return todos


@router.post("/",response_model=ToDoResponse)
def create_todo(todo:ToDo):
    todos.append(todo)
    return {"message":"ToDo created succesfully"}


@router.put('/{todo_id}')
def update_todo(todo_id: int, updated_todo:ToDo):
    for i, todo in enumerate(todos):
        if todo.id==todo_id:
            todos[i]=updated_todo
            return {"message":"your todo has been updated"}
    return{"message":"failed to update the todo"}


@router.delete('/{todo_id}')
def delete_todo(todo_id:int):
    global todos
    todos=[todo for todo in todos if todo.id!=todo_id]
    return{"message":"Todo Deleted successfully"}
            