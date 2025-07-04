from pydantic import BaseModel
from typing import List, Optional

class PatientCreate(BaseModel):
    name: str
    last_name: str
    dob: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    mobile: Optional[str]
    email: Optional[str]
    refere_by_doctor: Optional[str]
    consultant: Optional[str]
    test_list: List[int]
    total_amount: Optional[float]
    paid_amount: Optional[float]
    discount: Optional[str]
    other_amount: Optional[float]
    remark: Optional[str]
    

class PatientOut(BaseModel):
    id: int
    name: str
    last_name: str
    dob: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    created_at: Optional[str]
    mobile: Optional[str]
    email: Optional[str]
    refere_by_doctor: Optional[str]
    consultant: Optional[str]
    total_amount: Optional[float]
    paid_amount: Optional[float]
    balance_amount: Optional[float]
    discount: Optional[float]
    other_amount: Optional[float]
    remark: Optional[str]
    test_list: Optional[List[int]]

class PatientUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    dob: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    mobile: Optional[str]
    email: Optional[str]
    refere_by_doctor: Optional[str]
    consultant: Optional[str]
    total_amount: Optional[float]
    paid_amount: Optional[float]
    balance_amount: Optional[float]
    discount: Optional[float]
    other_amount: Optional[float]
    remark: Optional[str]
    test_list: Optional[List[int]]


class DoctorCreate(BaseModel):
    name: str
    designation: str
    degree: str
    mobile: str

class DoctorOut(BaseModel):
    id: int
    name: str
    designation: str
    degree: str
    mobile: str

class DoctorUpdate(BaseModel):
    name: Optional[str]
    designation: Optional[str]
    degree: Optional[str]
    mobile: Optional[str]

class TestCreate(BaseModel):
    name: str
    description: Optional[str]
    parameters: Optional[str]

class TestOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    parameters: Optional[str]

class TestUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    parameters: Optional[str]