import requests
from datetime import datetime
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse, StreamingResponse

from config import API_TOKEN_DNI, USUARIOS_AUTORIZADOS
from database import db_registros
from views import html_login, html_menu_principal, html_modulo_ciudadanos, html_modulo_detenidos
from pdf_generator import generar_pdf_ciudadanos, generar_pdf_detenidos_landscape

router = APIRouter()

def obtener_usuario_actual(request: Request):
    return request.session.get("usuario")

# --- CONSULTA DNI ---
@router.get("/buscar-dni/{dni}")
def buscar_dni(dni: str):
    if len(dni) != 8 or not dni.isdigit():
        return JSONResponse(status_code=400, content={"success": False, "message": "DNI debe tener 8 dígitos numéricos."})
    
    try:
        url = f"https://dniruc.apisperu.com/api/v1/dni/{dni}"
        headers = {"Authorization": f"Bearer {API_TOKEN_DNI}", "Accept": "application/json"}
        params = {"token": API_TOKEN_DNI}
        
        response = requests.get(url, headers=headers, params=params, timeout=5)
        if response.status_code == 200:
            datos = response.json()
            nombres = datos.get("nombres", "")
            paterno = datos.get("apellidoPaterno", "")
            materno = datos.get("apellidoMaterno", "")
            nombre_completo = f"{nombres} {paterno} {materno}".strip()
            
            if nombre_completo:
                return {"success": True, "nombre": nombre_completo}
            else:
                return {"success": False, "message": "DNI no encontrado."}
        else:
            return {"success": False, "message": "Error de verificación DNI."}
            
    except Exception:
        return {"success": False, "message": "Error de conexión con la API."}

# --- LOGIN Y NAVEGACIÓN ---
@router.get("/login", response_class=HTMLResponse)
def vista_login(request: Request, error: str = None):
    return html_login(error)

@router.post("/login")
def procesar_login(request: Request, usuario: str = Form(...), password: str = Form(...)):
    if usuario in USUARIOS_AUTORIZADOS and USUARIOS_AUTORIZADOS[usuario] == password:
        request.session["usuario"] = usuario
        return RedirectResponse(url="/menu", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/login?error=Usuario+o+contrase%C3%B1a+incorrectos", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/logout")
def cerrar_sesion(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/", response_class=HTMLResponse)
@router.get("/menu", response_class=HTMLResponse)
def menu(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    return html_menu_principal(usuario)

@router.get("/registro-ciudadanos", response_class=HTMLResponse)
def modulo_ciudadanos(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    return html_modulo_ciudadanos(usuario, db_registros)

@router.get("/registro-detenidos", response_class=HTMLResponse)
def modulo_detenidos(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    return html_modulo_detenidos(usuario, db_registros)

# --- ACCIONES DE REGISTRO Y SALIDA ---
@router.post("/registrar")
def registrar(
    request: Request, 
    origen: str = Form("ciudadanos"),
    dni: str = Form(...), 
    nombre: str = Form(...), 
    situacion: str = Form(...), 
    motivo: str = Form(...), 
    destino: str = Form(...),
    instructor: str = Form(None)
):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

    nuevo_id = len(db_registros) + 1
    hora_actual = datetime.now().strftime("%I:%M %p")
    
    db_registros.append({
        "id": nuevo_id,
        "dni": dni,
        "nombre": nombre.upper(),
        "situacion": situacion,
        "motivo": motivo,
        "destino": destino,
        "instructor": instructor.upper() if instructor else None,
        "hora_ingreso": hora_actual,
        "hora_salida": None
    })
    
    redireccion = "/registro-detenidos" if origen == "detenidos" else "/registro-ciudadanos"
    return RedirectResponse(url=redireccion, status_code=status.HTTP_303_SEE_OTHER)

@router.post("/marcar-salida")
def marcar_salida(request: Request, registro_id: int = Form(...), origen: str = Form("ciudadanos")):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

    hora_actual = datetime.now().strftime("%I:%M %p")
    for r in db_registros:
        if r["id"] == registro_id:
            r["hora_salida"] = hora_actual
            break
            
    redireccion = "/registro-detenidos" if origen == "detenidos" else "/registro-ciudadanos"
    return RedirectResponse(url=redireccion, status_code=status.HTTP_303_SEE_OTHER)

# --- EXPORTACIONES PDF ---
@router.get("/exportar-pdf-ciudadanos")
def pdf_ciudadanos(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

    pdf_buffer = generar_pdf_ciudadanos(db_registros)
    return StreamingResponse(
        pdf_buffer, 
        media_type="application/pdf", 
        headers={"Content-Disposition": "attachment; filename=Reporte_Ciudadanos_Pichanaqui.pdf"}
    )

@router.get("/exportar-pdf-detenidos")
def pdf_detenidos(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

    pdf_buffer = generar_pdf_detenidos_landscape(db_registros)
    return StreamingResponse(
        pdf_buffer, 
        media_type="application/pdf", 
        headers={"Content-Disposition": "attachment; filename=Reporte_Detenidos_Pichanaqui_Horizontal.pdf"}
    )