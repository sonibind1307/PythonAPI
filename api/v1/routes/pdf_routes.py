from fastapi import APIRouter
from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

router = APIRouter()

PDF_FOLDER = "generated_pdfs"
os.makedirs(PDF_FOLDER, exist_ok=True)

@router.get("/create-pdf/{patient_id}")
def create_pdf(patient_id: int):
    # Example: generate a simple PDF
    filename = f"patient_{patient_id}.pdf"
    filepath = os.path.join(PDF_FOLDER, filename)

    c = canvas.Canvas(filepath, pagesize=letter)
    c.drawString(100, 750, f"Patient Report for Patient ID: {patient_id}")
    c.drawString(100, 730, "Name: Soni Bind")
    c.drawString(100, 710, "Details: Example generated PDF.")
    c.showPage()
    c.save()

    # Return URL to access the PDF
    url = f"/api/v1/pdf/get-pdf/{filename}"
    return {"pdf_url": url}

@router.get("/get-pdf/{filename}")
def get_pdf(filename: str):
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    filepath = os.path.join("generated_pdfs", filename)
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="application/pdf")
    else:
        return {"error": "File not found"}
