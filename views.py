
def html_login(error: str = None):
    mensaje_error = f'<div class="alert alert-danger shadow-sm rounded-3" role="alert">{error}</div>' if error else ''
    url_fondo = "/static/fondo.jpg"
    
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login - Comisaría PNP Pichanaqui</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(rgba(0, 30, 15, 0.75), rgba(0, 15, 5, 0.85)), url('{url_fondo}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                min-height: 100vh;
            }}
            .card-login {{
                background: rgba(255, 255, 255, 0.96);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.3);
            }}
            .btn-pnp {{
                background-color: #006633;
                border-color: #004d26;
                color: #ffffff;
                transition: all 0.3s ease;
            }}
            .btn-pnp:hover {{
                background-color: #004d26;
                color: #ffffff;
                transform: translateY(-2px);
                box-shadow: 0 6px 15px rgba(0, 102, 51, 0.4);
            }}
        </style>
    </head>
    <body class="d-flex align-items-center justify-content-center p-3">
        <div class="card card-login shadow-lg p-4 p-md-5" style="width: 100%; max-width: 440px;">
            <div class="text-center mb-4">
                <div class="badge bg-success mb-2 px-3 py-2 rounded-pill fs-7">SISTEMA PNP 2026</div>
                <h4 class="fw-bold text-success mb-1" style="color: #006633 !important;">COMISARÍA PNP PICHANAQUI</h4>
                <p class="text-muted small">Control Digital de Ciudadanos y Detenidos</p>
            </div>
            {mensaje_error}
            <form action="/login" method="post">
                <div class="form-floating mb-3">
                    <input type="text" name="usuario" class="form-control rounded-3" id="floatingUser" placeholder="Usuario" required>
                    <label for="floatingUser">👤 Usuario / CIP</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" name="password" class="form-control rounded-3" id="floatingPassword" placeholder="Contraseña" required>
                    <label for="floatingPassword">🔒 Contraseña</label>
                </div>
                <button type="submit" class="btn btn-pnp w-100 py-3 rounded-3 fw-bold mt-2 fs-6">Ingresar al Sistema</button>
            </form>
            <div class="text-center mt-4">
                <span class="text-muted style-italic" style="font-size: 0.78rem;">
                    "Año de la Esperanza y el Fortalecimiento de la Democracia"
                </span>
            </div>
        </div>
    </body>
    </html>
    """

def html_menu_principal(usuario: str):
    url_fondo = "/static/fondo.jpg"
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Menú Principal - Comisaría Pichanaqui</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(rgba(0, 30, 15, 0.75), rgba(0, 15, 5, 0.85)), url('{url_fondo}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                min-height: 100vh;
            }}
            .card-interactive {{
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(12px);
                border-radius: 24px;
                border: 1px solid rgba(255, 255, 255, 0.4);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}
            .card-interactive:hover {{
                transform: translateY(-8px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4) !important;
            }}
            .bg-pnp {{
                background-color: #006633 !important;
            }}
            .btn-pnp {{
                background-color: #006633;
                border-color: #004d26;
                color: #ffffff;
            }}
            .btn-pnp:hover {{
                background-color: #004d26;
                color: #ffffff;
            }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-pnp mb-4 shadow-lg py-3">
            <div class="container">
                <span class="navbar-brand fw-bold fs-5">🛡️ Comisaría PNP Pichanaqui</span>
                <div class="d-flex align-items-center">
                    <span class="badge bg-light text-dark me-3 px-3 py-2 rounded-pill fs-7">👮 Efectivo: <b>{usuario}</b></span>
                    <a href="/logout" class="btn btn-outline-light btn-sm rounded-pill px-3">Cerrar Sesión</a>
                </div>
            </div>
        </nav>

        <div class="container text-center py-3">
            <div class="mb-4">
                <p class="text-warning small mb-1 fw-semibold">
                    "Año de la Esperanza y el Fortalecimiento de la Democracia" (2026)
                </p>
                <h2 class="fw-bold text-white display-6">SISTEMA DIGITAL DE CONTROL Y REGISTRO</h2>
                <p class="text-light opacity-75">Seleccione el módulo operativo al que desea acceder</p>
            </div>

            <div class="row justify-content-center g-4 my-2">
                <!-- Tarjeta 1: Registrar Ciudadano -->
                <div class="col-md-5">
                    <div class="card card-interactive shadow-lg h-100 p-4">
                        <div class="card-body d-flex flex-column justify-content-between text-center">
                            <div>
                                <div class="display-3 text-success mb-3">👤</div>
                                <h3 class="card-title fw-bold text-success mb-3" style="color: #006633 !important;">REGISTRAR CIUDADANO</h3>
                                <p class="card-text text-muted">
                                    Módulo dinámico para el control de ingreso y salida de denunciantes, recurrentes, citados y visitas.
                                </p>
                            </div>
                            <a href="/registro-ciudadanos" class="btn btn-pnp btn-lg w-100 fw-bold mt-4 py-3 rounded-pill shadow-sm">
                                INGRESAR AL MÓDULO ➔
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Tarjeta 2: Registrar Detenido -->
                <div class="col-md-5">
                    <div class="card card-interactive shadow-lg h-100 p-4">
                        <div class="card-body d-flex flex-column justify-content-between text-center">
                            <div>
                                <div class="display-3 text-warning mb-3">🚨</div>
                                <h3 class="card-title fw-bold text-dark mb-3">REGISTRAR DETENIDO</h3>
                                <p class="card-text text-muted">
                                    Módulo especializado para la Custodia de Detenidos/Retenidos e asignación de Instructor PNP a cargo.
                                </p>
                            </div>
                            <a href="/registro-detenidos" class="btn btn-dark btn-lg w-100 fw-bold mt-4 py-3 rounded-pill shadow-sm">
                                INGRESAR AL MÓDULO ➔
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

def html_modulo_ciudadanos(usuario: str, db_registros: list):
    url_fondo = "/static/fondo.jpg"
    ciudadanos = [r for r in db_registros if r.get("situacion") in ["DENUNCIANTE", "RECURRENTE"]]
    filas_html = ""
    for r in ciudadanos:
        if r["hora_salida"]:
            salida_html = f"<span class='badge bg-secondary px-3 py-2 rounded-pill fs-7'>🚪 Salida: {r['hora_salida']}</span>"
        else:
            salida_html = f"""
            <form action="/marcar-salida" method="post" style="display:inline;">
                <input type="hidden" name="registro_id" value="{r['id']}">
                <input type="hidden" name="origen" value="ciudadanos">
                <button type="submit" class="btn btn-success btn-sm fw-bold rounded-pill px-3 shadow-sm btn-hover-elevate">🚪 Marcar Salida</button>
            </form>
            """
        sit = r.get("situacion", "RECURRENTE")
        badge_sit = f"<span class='badge bg-warning text-dark px-3 py-2 rounded-pill shadow-sm'>⚠️ {sit}</span>" if sit == "DENUNCIANTE" else f"<span class='badge bg-info text-dark px-3 py-2 rounded-pill shadow-sm'>👤 {sit}</span>"
            
        filas_html += f"""
        <tr>
            <td class="fw-bold text-success" style="color: #006633 !important;">{r['dni']}</td>
            <td class="fw-semibold text-dark">{r['nombre']}</td>
            <td>{badge_sit}</td>
            <td><span class="badge bg-light text-dark border">{r['motivo']}</span></td>
            <td><span class="badge bg-light text-dark border">{r['destino']}</span></td>
            <td><span class="badge bg-pnp text-white px-2 py-1 rounded-3">🕒 {r['hora_ingreso']}</span></td>
            <td>{salida_html}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Control de Ciudadanos - Comisaría Pichanaqui</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(rgba(0, 30, 15, 0.75), rgba(0, 15, 5, 0.85)), url('{url_fondo}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                min-height: 100vh;
            }}
            .card-content {{
                background: rgba(255, 255, 255, 0.97);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.4);
            }}
            .bg-pnp {{
                background-color: #006633 !important;
            }}
            .btn-pnp {{
                background-color: #006633;
                border-color: #004d26;
                color: #ffffff;
                transition: all 0.3s ease;
            }}
            .btn-pnp:hover {{
                background-color: #004d26;
                color: #ffffff;
                transform: translateY(-2px);
                box-shadow: 0 6px 15px rgba(0, 102, 51, 0.3);
            }}
            .btn-hover-elevate:hover {{
                transform: translateY(-2px);
                transition: all 0.2s ease;
            }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-pnp mb-4 shadow-lg">
            <div class="container">
                <a href="/menu" class="btn btn-outline-light btn-sm rounded-pill px-3 me-3">⬅ Menú Principal</a>
                <span class="navbar-brand fw-bold">🛡️ Comisaría PNP Pichanaqui - Módulo Ciudadanos</span>
                <div class="d-flex align-items-center">
                    <span class="badge bg-light text-dark me-3 px-3 py-2 rounded-pill shadow-sm">👮 Efectivo: <b>{usuario}</b></span>
                    <a href="/logout" class="btn btn-outline-light btn-sm rounded-pill px-3">Cerrar Sesión</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <div>
                    <h3 class="text-white fw-bold mb-0">👥 Control de Ingreso y Salida de Ciudadanos</h3>
                    <small class="text-warning fw-semibold">"Año de la Esperanza y el Fortalecimiento de la Democracia" (2026)</small>
                </div>
                <a href="/exportar-pdf-ciudadanos" class="btn btn-pnp fw-bold rounded-pill shadow px-4 py-2" target="_blank">📄 Exportar Reporte (PDF)</a>
            </div>

            <!-- Formulario Moderno -->
            <div class="card card-content shadow-lg mb-4">
                <div class="card-header bg-pnp text-white py-3 d-flex justify-content-between align-items-center" style="border-radius: 20px 20px 0 0;">
                    <h5 class="mb-0 fw-bold">📝 Registrar Nuevo Ciudadano</h5>
                    <small id="estado_dni" class="text-warning fw-bold fs-7"></small>
                </div>
                <div class="card-body p-4">
                    <form action="/registrar" method="post" class="row g-3">
                        <input type="hidden" name="origen" value="ciudadanos">
                        <div class="col-md-3">
                            <div class="form-floating">
                                <input type="text" id="dni_input" name="dni" class="form-control rounded-3" maxlength="8" required placeholder="DNI">
                                <label for="dni_input">💳 DNI / Documento</label>
                            </div>
                            <button type="button" id="btn_buscar_persona" class="btn btn-warning btn-sm w-100 mt-2 fw-bold rounded-3 shadow-sm btn-hover-elevate">
                                🔍 BUSCAR RENIEC
                            </button>
                        </div>
                        <div class="col-md-4">
                            <div class="form-floating">
                                <input type="text" id="nombre_input" name="nombre" class="form-control rounded-3" required placeholder="Nombres">
                                <label for="nombre_input">👤 Nombres y Apellidos</label>
                            </div>
                        </div>
                        <div class="col-md-2">
                            <div class="form-floating">
                                <select name="situacion" class="form-select rounded-3 fw-bold" id="floatingSit" required>
                                    <option value="DENUNCIANTE">DENUNCIANTE</option>
                                    <option value="RECURRENTE" selected>RECURRENTE</option>
                                </select>
                                <label for="floatingSit">📋 Situación</label>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="form-floating">
                                <select name="motivo" class="form-select rounded-3" id="floatingMotivo">
                                    <option value="Denuncia">Denuncia</option>
                                    <option value="Trámite / Citación">Trámite / Citación</option>
                                    <option value="Otro">Otro</option>
                                </select>
                                <label for="floatingMotivo">📌 Motivo de Visita</label>
                            </div>
                        </div>
                        <div class="col-md-12">
                            <div class="form-floating">
                                <select name="destino" class="form-select rounded-3" id="floatingDestino">
                                    <option value="Secretaría">Secretaría</option>
                                    <option value="Delitos y Faltas">Delitos y Faltas</option>
                                    <option value="Accidentes de Tránsito">Accidentes de Tránsito</option>
                                    <option value="Familia">Familia / Medidas de Protección</option>
                                </select>
                                <label for="floatingDestino">🏢 Sección o Área de Destino</label>
                            </div>
                        </div>
                        <div class="col-12 text-end mt-4">
                            <button type="submit" class="btn btn-pnp fw-bold rounded-pill px-5 py-2 fs-6 shadow">✅ Registrar Ingreso</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Tabla de Registros -->
            <div class="card card-content shadow-lg mb-5">
                <div class="card-header bg-dark text-white py-3 d-flex justify-content-between align-items-center" style="border-radius: 20px 20px 0 0;">
                    <h5 class="mb-0 fw-bold">📋 Listado de Ciudadanos Registrados</h5>
                    <span class="badge bg-secondary rounded-pill">Sistema Digital Pichanaqui</span>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-hover mb-0 text-center align-middle">
                            <thead class="table-light">
                                <tr class="text-secondary small text-uppercase">
                                    <th>DNI</th>
                                    <th>Nombres y Apellidos</th>
                                    <th>Situación</th>
                                    <th>Motivo</th>
                                    <th>Destino</th>
                                    <th>Hora Ingreso</th>
                                    <th>Acción / Estado Salida</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filas_html}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <script>
            async function ejecutarBusquedaDNI() {{
                let dni = document.getElementById("dni_input").value.trim();
                let campoNombre = document.getElementById("nombre_input");
                let estadoDni = document.getElementById("estado_dni");
                let btnBuscar = document.getElementById("btn_buscar_persona");

                if (dni.length !== 8 || !/^\\d+$/.test(dni)) {{
                    alert("Por favor, ingrese un DNI válido de 8 dígitos.");
                    return;
                }}

                estadoDni.innerText = "🔍 Buscando en RENIEC...";
                campoNombre.value = "Consultando...";
                btnBuscar.disabled = true;

                try {{
                    let res = await fetch(`/buscar-dni/${{dni}}`);
                    let data = await res.json();

                    if (data.success && data.nombre) {{
                        campoNombre.value = data.nombre;
                        estadoDni.innerText = "✅ Datos cargados correctamente";
                    }} else {{
                        campoNombre.value = "";
                        estadoDni.innerText = "⚠️ DNI no encontrado.";
                        alert(data.message || "DNI no encontrado.");
                    }}
                }} catch (error) {{
                    campoNombre.value = "";
                    estadoDni.innerText = "⚠️ Error de red.";
                }} finally {{
                    btnBuscar.disabled = false;
                }}
            }}

            document.getElementById("btn_buscar_persona").addEventListener("click", ejecutarBusquedaDNI);
        </script>
    </body>
    </html>
    """

def html_modulo_detenidos(usuario: str, db_registros: list):
    url_fondo = "/static/fondo.jpg"
    detenidos = [r for r in db_registros if r.get("situacion") in ["DETENIDO", "RETENIDO"]]

    filas_html = ""
    for r in detenidos:
        if r["hora_salida"]:
            salida_html = f"<span class='badge bg-secondary px-3 py-2 rounded-pill fs-7'>🚪 Salida: {r['hora_salida']}</span>"
        else:
            salida_html = f"""
            <form action="/marcar-salida" method="post" style="display:inline;">
                <input type="hidden" name="registro_id" value="{r['id']}">
                <input type="hidden" name="origen" value="detenidos">
                <button type="submit" class="btn btn-warning btn-sm fw-bold rounded-pill px-3 shadow-sm btn-hover-elevate">🔓 Registrar Libertad / Disposición</button>
            </form>
            """
        
        badge_sit = f"<span class='badge bg-danger px-3 py-2 rounded-pill fs-7 shadow-sm'>🚨 {r['situacion']}</span>"
        instructor_txt = r.get("instructor", "NO REGISTRADO")
            
        filas_html += f"""
        <tr>
            <td class="fw-bold text-danger">{r['dni']}</td>
            <td class="fw-semibold text-dark">{r['nombre']}</td>
            <td>{badge_sit}</td>
            <td><span class="badge bg-light text-dark border">{r['motivo']}</span></td>
            <td><span class="badge bg-light text-dark border">{r['destino']}</span></td>
            <td><span class="fw-bold text-success border-bottom border-success border-2">{instructor_txt}</span></td>
            <td><span class="badge bg-dark text-white px-2 py-1 rounded-3">🕒 {r['hora_ingreso']}</span></td>
            <td>{salida_html}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Custodia de Detenidos - Comisaría Pichanaqui</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(rgba(0, 30, 15, 0.75), rgba(0, 15, 5, 0.85)), url('{url_fondo}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                min-height: 100vh;
            }}
            .card-content {{
                background: rgba(255, 255, 255, 0.97);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.4);
            }}
            .bg-pnp {{
                background-color: #006633 !important;
            }}
            .btn-pnp {{
                background-color: #006633;
                border-color: #004d26;
                color: #ffffff;
                transition: all 0.3s ease;
            }}
            .btn-pnp:hover {{
                background-color: #004d26;
                color: #ffffff;
                transform: translateY(-2px);
                box-shadow: 0 6px 15px rgba(0, 102, 51, 0.3);
            }}
            .btn-hover-elevate:hover {{
                transform: translateY(-2px);
                transition: all 0.2s ease;
            }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-pnp mb-4 shadow-lg">
            <div class="container">
                <a href="/menu" class="btn btn-outline-light btn-sm rounded-pill px-3 me-3">⬅ Menú Principal</a>
                <span class="navbar-brand fw-bold">🚨 Comisaría PNP Pichanaqui - Custodia de Detenidos</span>
                <div class="d-flex align-items-center">
                    <span class="badge bg-light text-dark me-3 px-3 py-2 rounded-pill shadow-sm">👮 Efectivo: <b>{usuario}</b></span>
                    <a href="/logout" class="btn btn-outline-light btn-sm rounded-pill px-3">Cerrar Sesión</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <div>
                    <h3 class="text-white fw-bold mb-0">🚨 Registro y Custodia de Detenidos / Retenidos</h3>
                    <small class="text-warning fw-semibold">"Año de la Esperanza y el Fortalecimiento de la Democracia" (2026)</small>
                </div>
                <a href="/exportar-pdf-detenidos" class="btn btn-pnp fw-bold rounded-pill shadow px-4 py-2" target="_blank">📄 Exportar Reporte Detenidos (PDF)</a>
            </div>

            <!-- Formulario Moderno -->
            <div class="card card-content shadow-lg mb-4">
                <div class="card-header bg-pnp text-white py-3 d-flex justify-content-between align-items-center" style="border-radius: 20px 20px 0 0;">
                    <h5 class="mb-0 fw-bold">📝 Registrar Personas en Custodia Legal</h5>
                    <small id="estado_dni" class="text-warning fw-bold fs-7"></small>
                </div>
                <div class="card-body p-4">
                    <form action="/registrar" method="post" class="row g-3">
                        <input type="hidden" name="origen" value="detenidos">
                        <div class="col-md-3">
                            <div class="form-floating">
                                <input type="text" id="dni_input" name="dni" class="form-control rounded-3" maxlength="8" required placeholder="DNI">
                                <label for="dni_input">💳 DNI / Documento</label>
                            </div>
                            <button type="button" id="btn_buscar_persona" class="btn btn-warning btn-sm w-100 mt-2 fw-bold rounded-3 shadow-sm btn-hover-elevate">
                                🔍 BUSCAR RENIEC
                            </button>
                        </div>
                        <div class="col-md-4">
                            <div class="form-floating">
                                <input type="text" id="nombre_input" name="nombre" class="form-control rounded-3" required placeholder="Nombres">
                                <label for="nombre_input">👤 Nombres y Apellidos</label>
                            </div>
                        </div>
                        <div class="col-md-2">
                            <div class="form-floating">
                                <select name="situacion" class="form-select rounded-3 fw-bold bg-warning" id="floatingSitDet" required>
                                    <option value="DETENIDO" selected>DETENIDO</option>
                                    <option value="RETENIDO">RETENIDO</option>
                                </select>
                                <label for="floatingSitDet">⚖️ Condición Legal</label>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="form-floating">
                                <select name="motivo" class="form-select rounded-3" id="floatingMotivoDet">
                                    <option value="Intervención Policial">Intervención Policial</option>
                                    <option value="Delito Flagrante">Delito Flagrante</option>
                                    <option value="Mandato Judicial">Mandato Judicial</option>
                                </select>
                                <label for="floatingMotivoDet">📌 Motivo Detención</label>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="form-floating">
                                <select name="destino" class="form-select rounded-3" id="floatingDestinoDet">
                                    <option value="Custodia de Detenidos" selected>Custodia de Detenidos (Calabozo)</option>
                                    <option value="Delitos y Faltas">Delitos y Faltas</option>
                                    <option value="Accidentes de Tránsito">Accidentes de Tránsito</option>
                                    <option value="Familia">Familia</option>
                                </select>
                                <label for="floatingDestinoDet">🏢 Sección a Cargo</label>
                            </div>
                        </div>
                        <div class="col-md-8">
                            <div class="form-floating">
                                <input type="text" name="instructor" id="floatingInstructor" class="form-control rounded-3 border-success" required placeholder="Instructor PNP">
                                <label for="floatingInstructor" class="text-success fw-bold">👮 Instructor PNP a Cargo (Grado y Nombres)</label>
                            </div>
                        </div>
                        <div class="col-12 text-end mt-4">
                            <button type="submit" class="btn btn-pnp fw-bold rounded-pill px-5 py-2 fs-6 shadow">✅ Registrar Ingreso de Detenido</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Tabla de Registros -->
            <div class="card card-content shadow-lg mb-5">
                <div class="card-header bg-dark text-white py-3 d-flex justify-content-between align-items-center" style="border-radius: 20px 20px 0 0;">
                    <h5 class="mb-0 fw-bold">📋 Listado de Personas en Custodia (Calabozo)</h5>
                    <span class="badge bg-danger rounded-pill">Custodia Temporal PNP</span>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-hover mb-0 text-center align-middle">
                            <thead class="table-light">
                                <tr class="text-secondary small text-uppercase">
                                    <th>DNI</th>
                                    <th>Nombres y Apellidos</th>
                                    <th>Condición Legal</th>
                                    <th>Motivo</th>
                                    <th>Sección</th>
                                    <th>Instructor PNP A Cargo</th>
                                    <th>Hora Ingreso</th>
                                    <th>Acción / Estado Salida</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filas_html}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <script>
            async function ejecutarBusquedaDNI() {{
                let dni = document.getElementById("dni_input").value.trim();
                let campoNombre = document.getElementById("nombre_input");
                let estadoDni = document.getElementById("estado_dni");
                let btnBuscar = document.getElementById("btn_buscar_persona");

                if (dni.length !== 8 || !/^\\d+$/.test(dni)) {{
                    alert("Por favor, ingrese un DNI válido de 8 dígitos.");
                    return;
                }}

                estadoDni.innerText = "🔍 Buscando en RENIEC...";
                campoNombre.value = "Consultando...";
                btnBuscar.disabled = true;

                try {{
                    let res = await fetch(`/buscar-dni/${{dni}}`);
                    let data = await res.json();

                    if (data.success && data.nombre) {{
                        campoNombre.value = data.nombre;
                        estadoDni.innerText = "✅ Datos cargados correctamente";
                    }} else {{
                        campoNombre.value = "";
                        estadoDni.innerText = "⚠️ DNI no encontrado.";
                        alert(data.message || "DNI no encontrado.");
                    }}
                }} catch (error) {{
                    campoNombre.value = "";
                    estadoDni.innerText = "⚠️ Error de red.";
                }} finally {{
                    btnBuscar.disabled = false;
                }}
            }}

            document.getElementById("btn_buscar_persona").addEventListener("click", ejecutarBusquedaDNI);
        </script>
    </body>
    </html>
    """