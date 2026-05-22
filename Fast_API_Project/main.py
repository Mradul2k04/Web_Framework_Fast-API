from fastapi import FastAPI
from crud import router as crud_router

app=FastAPI()


app.include_router(crud_router,prefix='/todo',tags={"Curd Router"})