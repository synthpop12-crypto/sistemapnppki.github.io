from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from config import SECRET_KEY
from routes import router

app = FastAPI(title="Sistema Web - Comisaría PNP Pichanaqui")

# 1. Configurar la carpeta de archivos estáticos (imágenes, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Middleware de seguridad para la sesión
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# 3. Registrar rutas centralizadas
app.include_router(router)