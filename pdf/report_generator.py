from reportlab.pdfgen import canvas
from io import BytesIO

def generate_report(data: dict):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 800, "Intelligence Report")
    c.drawString(100, 780, f"Session Data: {data}")
    c.save()
    buffer.seek(0)
    return buffer.getvalue()