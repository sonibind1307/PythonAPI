from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import json
import os

from api.v1.routes.patient_routes import router as patient_router
from api.v1.routes.doctor_routes import router as doctor_router
from api.v1.routes.test_routes import router as test_router
from api.v1.routes.pdf_routes import router as pdf_router



app = FastAPI(
    title="Healthcare API",
    description="A Clean Architecture FastAPI example for Hospitality/Healthcare",
    version="1.0.0")



origins = [
    "http://localhost:52045",
    "http://127.0.0.1:52045",
    "http://localhost:3000",  # your frontend origin
    "http://127.0.0.1:3000",  # just in case you use 127.0.0.1
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Allowed frontend origins
    allow_credentials=True,
    allow_methods=["*"],           # Allow all HTTP methods
    allow_headers=["*"],           # Allow all headers
)

app.include_router(patient_router, prefix="/api/v1/patients", tags=["Patients"])
app.include_router(doctor_router, prefix="/api/v1/doctors", tags=["Doctors"])
app.include_router(test_router, prefix="/api/v1/tests", tags=["Tests"])
app.include_router(pdf_router, prefix="/api/v1/pdf", tags=["PDF"])

@app.get("/")
def read_root():
    return {"message": "It works!"}

# Path to store the status file
STATUS_FILE = "status.json"

# Helper function to write status
def write_status(data):
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f)

# Helper function to read status
def read_status():
    if not os.path.exists(STATUS_FILE):
        return None
    with open(STATUS_FILE, "r") as f:
        return json.load(f)

# API 1: Start the update task
@app.post("/start-task")
def start_task():
    data = {
        "status": "in_progress",
        "start_time": datetime.utcnow().isoformat()
    }
    write_status(data)
    return {"message": "Task started!", "data": data}

# API 2: Check the task status
@app.get("/check-status")
def check_status():
    data = read_status()
    if not data:
        return {"message": "No task found."}

    start_time = datetime.fromisoformat(data["start_time"])
    now = datetime.utcnow()
    elapsed = now - start_time

    if elapsed >= timedelta(minutes=5):
        data["status"] = "completed"
        write_status(data)
        return {"message": "Task completed!", "data": data}
    else:
        remaining = timedelta(minutes=5) - elapsed
        return {
            "message": "Task still in progress.",
            "status": data["status"],
            "time_remaining_seconds": int(remaining.total_seconds())
        }
