from fastapi import APIRouter, HTTPException
from typing import List
from models.schemas import DoctorCreate, DoctorOut, DoctorUpdate
from services.doctor_service import DoctorService

router = APIRouter()
service = DoctorService()

@router.post("/", response_model=DoctorOut)
def create_doctor(doctor: DoctorCreate):
    doctor_id = service.create_doctor(doctor)
    created = service.get_doctor_by_id(doctor_id)
    return created

@router.get("/", response_model=List[DoctorOut])
def get_all_doctors():
    return service.get_all_doctors()

@router.get("/{doctor_id}", response_model=DoctorOut)
def get_doctor(doctor_id: int):
    doctor = service.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.put("/{doctor_id}", response_model=DoctorOut)
def update_doctor(doctor_id: int, doctor: DoctorUpdate):
    updated = service.update_doctor(doctor_id, doctor)
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated

@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int):
    doctor = service.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    service.delete_doctor(doctor_id)
    return {"message": "Doctor deleted successfully"}
