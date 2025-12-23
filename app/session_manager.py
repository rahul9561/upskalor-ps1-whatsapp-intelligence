from datetime import datetime, timedelta
from typing import Dict

sessions: Dict[str, dict] = {}  # phone_number -> {data, timestamp}

def get_session(phone: str):
    session = sessions.get(phone)
    if session and datetime.now() - session['timestamp'] < timedelta(minutes=10):
        return session['data']
    return {}

def update_session(phone: str, data: dict):
    sessions[phone] = {"data": data, "timestamp": datetime.now()}