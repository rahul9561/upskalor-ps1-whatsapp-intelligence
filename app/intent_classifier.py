# Placeholder - replace with your trained model (e.g., sklearn, transformers)
def classify_intent(text: str) -> str:
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "greeting"
    if "report" in text:
        return "request_report"
    if "help" in text:
        return "help"
    return "unknown"