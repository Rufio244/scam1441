from sqlalchemy import Column, String, Integer
from database import Base

class Case(Base):
    __tablename__ = "cases"
    
    id = Column(String, primary_key=True)
    bank_case_id = Column(String)
    citizen_id = Column(String)
    phone = Column(String)
    status = Column(String)
    scam_type = Column(String)
    risk_score = Column(String)
    assigned_station = Column(String)
