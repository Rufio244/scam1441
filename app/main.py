from fastapi import FastAPI
from routes import case, auth

app = FastAPI(title="SCAM1441 API")

app.include_router(case.router)
app.include_router(auth.router)
