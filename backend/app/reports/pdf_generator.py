from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    summary,
    action_items
):

    doc = SimpleDocTemplate(
        "meeting_report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Enterprise Meeting Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    summary_title = Paragraph(
        "Executive Summary",
        styles["Heading2"]
    )

    elements.append(summary_title)

    summary_para = Paragraph(
        summary,
        styles["BodyText"]
    )

    elements.append(summary_para)

    elements.append(Spacer(1, 20))

    action_title = Paragraph(
        "Action Items",
        styles["Heading2"]
    )

    elements.append(action_title)

    for item in action_items:

        para = Paragraph(
            f"• {item}",
            styles["BodyText"]
        )

        elements.append(para)

    doc.build(elements)

    return "meeting_report.pdf"