from fastapi import FastAPI
from Patient_routes.routes import router as patient_router

app = FastAPI(title="Patient Management System")

app.include_router(patient_router)