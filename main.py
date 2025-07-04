from fastapi import FastAPI
from api.v1.routes.patient_routes import router as patient_router
from api.v1.routes.doctor_routes import router as doctor_router
from api.v1.routes.test_routes import router as test_router

app = FastAPI(
    title="Healthcare API",
    description="A Clean Architecture FastAPI example for Hospitality/Healthcare",
    version="1.0.0")


app.include_router(patient_router, prefix="/api/v1/patients", tags=["Patients"])
app.include_router(doctor_router, prefix="/api/v1/doctors", tags=["Doctors"])
app.include_router(test_router, prefix="/api/v1/tests", tags=["Tests"])

@app.get("/")
def read_root():
    return {"message": "It works!"}