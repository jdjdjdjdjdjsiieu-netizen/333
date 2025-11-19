from pathlib import Path
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="Alfa Campaign Manager - Setup UI (dev)")


# Подключаем маршруты setup API, если он доступен
try:
    from setup_api import router as setup_router

    app.include_router(setup_router)
except Exception:
    # Если setup_api отсутствует или есть ошибки, игнорируем — endpoints не будут доступны
    pass


@app.get("/", response_class=HTMLResponse)
async def root():
    frontend_index = Path(__file__).parent / "build" / "index.html"
    if frontend_index.exists():
        return FileResponse(frontend_index)

    html = """
    <html>
      <head><title>Alfa Campaign Manager</title></head>
      <body>
        <h2>Alfa Campaign Manager</h2>
        <p>В разработке: интерфейс настройки доступен по <a href="/setup">/setup</a></p>
        <p>API конфигурации: <a href="/api/config">/api/config</a></p>
      </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)


@app.get("/setup", response_class=HTMLResponse)
async def setup_page():
    frontend_index = Path(__file__).parent / "build" / "index.html"
    if frontend_index.exists():
        return FileResponse(frontend_index)

    html = """
    <html>
      <head><title>Setup - Alfa</title></head>
      <body>
        <h2>Setup</h2>
        <p>Используйте API `/api/config` для просмотра и сохранения конфигурации.</p>
      </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)


@app.get("/health", tags=["health"])  # liveness
async def health():
    return {"status": "ok"}


@app.get("/health/ready", tags=["health"])  # readiness
async def readiness():
    db_file = Path(__file__).parent / "alfa.db"
    ready = db_file.exists()
    return {"ready": ready}


if os.path.isdir("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")
elif os.path.isdir("build"):
    app.mount("/static", StaticFiles(directory="build"), name="static")
