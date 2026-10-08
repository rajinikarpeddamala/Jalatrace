from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="JalaTrace")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "Frontend"

app.mount(
    "/static",
    StaticFiles(directory=str(FRONTEND_DIR)),
    name="static"
)

@app.get("/")
def home():
    return FileResponse(
        str(FRONTEND_DIR / "index.html")
    )

@app.get("/api/test")
def test_api():
    return {
        "message": "JalaTrace backend is working!"
    }