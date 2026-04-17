import requests
from config import settings

def send_to_police(case_data):
    try:
        res = requests.post(settings.POLICE_API, json=case_data)
        return res.json()
    except:
        return {"status": "mock_sent"}
