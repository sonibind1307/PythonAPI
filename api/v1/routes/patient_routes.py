from fastapi import APIRouter, HTTPException
from models.schemas import PatientCreate ,PatientOut,PatientUpdate
from services.patient_service import PatientService

router = APIRouter()
service = PatientService()

@router.post("/")
def create_patient(patient: PatientCreate):
    patient_id = service.create_patient(patient)
    return {"message": "Patient created", "patient_id": patient_id}

@router.get("/")
def get_all_patients():
    patients = service.get_all_patients()
    return patients

@router.get("/{patient_id}", response_model=PatientOut)
def get_patient(patient_id: int):
    patient = service.get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put("/{patient_id}", response_model=PatientOut)
def update_patient(patient_id: int, patient: PatientUpdate):
    updated = service.update_patient(patient_id, patient)
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated

@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    patient = service.get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    service.delete_patient(patient_id)
    return {"message": "Patient deleted successfully"}