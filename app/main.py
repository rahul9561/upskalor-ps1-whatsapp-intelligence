from fastapi import FastAPI, Request, Query, HTTPException
from .config import VERIFY_TOKEN
from .whatsapp_webhook import send_text
from .router import route_message
from .image_validator import is_handwritten_image
import httpx

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "PS1 service running"}

@app.get("/webhook")
async def verify(
    hub_mode: str = Query(alias="hub.mode"),
    hub_challenge: str = Query(alias="hub.challenge"),
    hub_verify_token: str = Query(alias="hub.verify_token")
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return hub_challenge
    raise HTTPException(status_code=403)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    if data.get("object") != "whatsapp_business_account":
        return {"status": "ignored"}

    for entry in data["entry"]:
        for change in entry["changes"]:
            value = change["value"]
            if "messages" in value:
                for msg in value["messages"]:
                    phone = msg["from"]
                    if msg.get("text"):
                        text = msg["text"]["body"]
                        response = await route_message(phone, text=text)
                        await send_text(phone, response)
                    elif msg.get("image"):
                        image_id = msg["image"]["id"]
                        # Download image
                        async with httpx.AsyncClient() as client:
                            img_resp = await client.get(f"{BASE_URL}/{image_id}", headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
                            img_url = img_resp.json()["url"]
                            img_data = await client.get(img_url)
                        valid = is_handwritten_image(img_data.content)
                        await send_text(phone, f"Handwriting validated: {'Yes' if valid else 'No'}")
    return {"status": "ok"}