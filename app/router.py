from .session_manager import get_session, update_session
from .intent_classifier import classify_intent

async def route_message(phone: str, text: str = None, image_url: str = None):
    intent = classify_intent(text) if text else "image"
    session = get_session(phone)

    if intent == "greeting":
        return "Hello! Send an image for validation or type 'report' for PDF."
    elif intent == "request_report":
        from pdf.report_generator import generate_report
        pdf_bytes = generate_report(session)
        # Upload PDF to WhatsApp and return media ID (implement upload)
        return "Here is your report!", pdf_bytes
    # Add more routing...
    return "I didn't understand that."