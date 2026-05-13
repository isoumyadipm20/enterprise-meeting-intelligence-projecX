from fastapi import APIRouter

from app.reports.pdf_generator import (
    generate_pdf_report
)

router = APIRouter()


@router.post("/generate-report")
def generate_report(data: dict):

    summary = data["summary"]

    action_items = data["action_items"]

    pdf_path = generate_pdf_report(
        summary,
        action_items
    )

    return {
        "report_generated": True,
        "file": pdf_path
    }