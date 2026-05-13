from fastapi import APIRouter

from app.nlp.summarizer import (
    generate_summary
)

from app.nlp.action_items import (
    extract_action_items
)

router = APIRouter()


@router.post("/summarize")
def summarize_meeting(data: dict):

    transcript = data["transcript"]

    summary = generate_summary(transcript)

    return {
        "summary": summary
    }


@router.post("/action-items")
def action_items(data: dict):

    transcript = data["transcript"]

    items = extract_action_items(
        transcript
    )

    return {
        "action_items": items
    }