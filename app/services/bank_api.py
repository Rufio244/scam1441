import requests
from config import settings

def freeze_account(bank, account_no, case_id):
    url_map = {
        "KBANK": settings.KBANK_API,
        "SCB": settings.SCB_API
    }
    
    payload = {
        "account": account_no,
        "reason": "SCAM",
        "case_id": case_id
    }
    
    try:
        res = requests.post(url_map[bank], json=payload)
        return res.json()
    except:
        return {"status": "mock_freeze_success"}
