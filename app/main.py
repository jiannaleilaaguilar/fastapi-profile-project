from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.api.v1.profile import router as profile_router

# Auto-create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Profile Feature")

# Mount profile router
app.include_router(profile_router)

# Resolve static directory relative to main.py
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get("/")
def read_root():
    return {"status": "Active", "message": "Visit /static/profile.html for the frontend UI."}
