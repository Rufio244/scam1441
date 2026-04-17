import os

class Settings:
    DB_URL = os.getenv("DB_URL", "postgresql://user:pass@localhost/scam1441")
    
    # BANK API (Mock / จริง)
    KBANK_API = os.getenv("KBANK_API", "https://api.kbank.com/freeze")
    SCB_API = os.getenv("SCB_API", "https://api.scb.co.th/freeze")
    
    # POLICE API
    POLICE_API = os.getenv("POLICE_API", "https://api.thaipoliceonline.go.th/case")
    
    # STORAGE
    STORAGE_PATH = "./uploads"
    
settings = Settings()
