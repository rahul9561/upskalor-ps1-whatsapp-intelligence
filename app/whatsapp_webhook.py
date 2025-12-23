from fastapi import Request, HTTPException
from .config import VERIFY_TOKEN, PHONE_NUMBER_ID, ACCESS_TOKEN
import httpx

BASE_URL = "https://graph.facebook.com/v20.0"

async def send_text(to: str, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{BASE_URL}/{PHONE_NUMBER_ID}/messages",
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
            json={
                "messaging_product": "whatsapp",
                "to": to,
                "type": "text",
                "text": {"body": text}
            }
        )

# Add send_image, send_document for PDF, etc.