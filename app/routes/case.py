from fastapi import APIRouter
import uuid
from services.ai import analyze_case
from services.router import route_case
from services.bank_api import freeze_account
from services.police_api import send_to_police

router = APIRouter()

@router.post("/case/confirm")
def confirm(data: dict):
    case_id = "SCAM1441-" + str(uuid.uuid4())[:8]
    
    scam_type, risk = analyze_case(data.get("text", ""))
    station = route_case(data["citizen_id"])
    
    # Freeze account
    freeze = freeze_account("KBANK", data.get("account", ""), case_id)
    
    # Send police
    police = send_to_police({
        "case_id": case_id,
        "type": scam_type,
        "risk": risk
    })
    
    return {
        "case_id": case_id,
        "scam_type": scam_type,
        "risk": risk,
        "station": station,
        "freeze": freeze,
        "police": police
    }
