from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Alfa Campaign Manager - Setup UI (dev)")

# Подключаем маршруты setup API, если он доступен
try:
    from setup_api import router as setup_router
    app.include_router(setup_router)
except Exception:
    # Если setup_api отсутствует или есть ошибки, игнорируем — endpoints не будут доступны
    pass

# Простая страница, перенаправляющая на /setup или на API UI
@app.get("/", response_class=HTMLResponse)
async def root():
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

# Маршрут /setup — возвращаем простую страницу с инструкциями
@app.get("/setup", response_class=HTMLResponse)
async def setup_page():
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

# Попробуем смонтировать папку `public` или `build` для фронтенда, если она есть
if os.path.isdir("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")
elif os.path.isdir("build"):
    app.mount("/static", StaticFiles(directory="build"), name="static")
