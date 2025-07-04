from fastapi import APIRouter, HTTPException
from typing import List
from models.schemas import TestCreate, TestOut, TestUpdate
from services.test_service import TestService

router = APIRouter()
service = TestService()

@router.post("/", response_model=TestOut)
def create_test(test: TestCreate):
    test_id = service.create_test(test)
    return service.get_test_by_id(test_id)

@router.get("/", response_model=List[TestOut])
def get_all_tests():
    return service.get_all_tests()

@router.get("/{test_id}", response_model=TestOut)
def get_test(test_id: int):
    test = service.get_test_by_id(test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test

@router.put("/{test_id}", response_model=TestOut)
def update_test(test_id: int, test: TestUpdate):
    updated = service.update_test(test_id, test)
    if not updated:
        raise HTTPException(status_code=404, detail="Test not found")
    return updated

@router.delete("/{test_id}")
def delete_test(test_id: int):
    test = service.get_test_by_id(test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    service.delete_test(test_id)
    return {"message": "Test deleted successfully"}
