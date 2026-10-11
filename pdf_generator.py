import io
from datetime import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ---------------------------------------------------------
# REPORTE 1: REGISTRO DE CIUDADANOS (ORIENTACIÓN VERTICAL VERDE PNP)
# ---------------------------------------------------------
def generar_pdf_ciudadanos(registros):
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    elements = []
    
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        alignment=1,
        textColor=colors.HexColor("#006633") # Verde PNP
    )
    
    style_meta = ParagraphStyle(
        'MetaStyle',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=1,
        textColor=colors.HexColor("#555555")
    )
    
    style_header = ParagraphStyle(
        'HeaderStyle',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=1,
        textColor=colors.whitesmoke
    )
    
    style_cell = ParagraphStyle(
        'CellStyle',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9,
        alignment=1
    )

    style_cell_bold = ParagraphStyle(
        'CellBoldStyle',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9,
        alignment=1
    )

    fecha_impresion = datetime.now().strftime("%d/%m/%Y %I:%M %p")

    title = Paragraph("<b>COMISARÍA PNP PICHANAQUI</b><br/><font size=9 color='gray'>LIBRO DIGITAL DE REGISTRO Y CONTROL DE CIUDADANOS</font>", style_title)
    elements.append(title)
    elements.append(Spacer(1, 4))
    
    meta_info = Paragraph(f"<b>FECHA Y HORA DE IMPRESIÓN:</b> {fecha_impresion}", style_meta)
    elements.append(meta_info)
    elements.append(Spacer(1, 12))
    
    headers = [
        Paragraph("DNI", style_header),
        Paragraph("Nombres y Apellidos", style_header),
        Paragraph("Situación", style_header),
        Paragraph("Motivo", style_header),
        Paragraph("Sección Destino", style_header),
        Paragraph("Ingreso", style_header),
        Paragraph("Salida / Estado", style_header)
    ]
    
    data = [headers]
    
    ciudadanos = [r for r in registros if r.get("situacion") in ["DENUNCIANTE", "RECURRENTE"]]
    
    for r in ciudadanos:
        estado_texto = r.get("hora_salida") if r.get("hora_salida") else "EN COMISARÍA"
        situacion_texto = r.get("situacion", "RECURRENTE")
        
        fila = [
            Paragraph(str(r.get("dni", "")), style_cell_bold),
            Paragraph(str(r.get("nombre", "")), style_cell),
            Paragraph(f"<b>{situacion_texto}</b>", style_cell),
            Paragraph(str(r.get("motivo", "")), style_cell),
            Paragraph(str(r.get("destino", "")), style_cell),
            Paragraph(str(r.get("hora_ingreso", "")), style_cell),
            Paragraph(estado_texto, style_cell)
        ]
        data.append(fila)
        
    col_widths = [55, 120, 75, 80, 85, 55, 70]
    
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#006633")), # Encabezado Verde PNP
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F2F9F4")])
    ]))
    
    elements.append(t)
    doc.build(elements)
    buffer.seek(0)
    return buffer


# ---------------------------------------------------------
# REPORTE 2: REGISTRO DE DETENIDOS (ORIENTACIÓN HORIZONTAL)
# ---------------------------------------------------------
def generar_pdf_detenidos_landscape(registros):
    buffer = io.BytesIO()
    
    # Formato Apaisado / Horizontal (Landscape)
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=landscape(letter),
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    elements = []
    
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=15,
        alignment=1,
        textColor=colors.HexColor("#8B0000") # Rojo Institucional
    )

    style_meta = ParagraphStyle(
        'MetaStyle',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10,
        alignment=1,
        textColor=colors.HexColor("#333333")
    )
    
    style_header = ParagraphStyle(
        'HeaderStyle',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=1,
        textColor=colors.whitesmoke
    )
    
    style_cell = ParagraphStyle(
        'CellStyle',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9,
        alignment=1
    )

    style_cell_bold = ParagraphStyle(
        'CellBoldStyle',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9,
        alignment=1
    )

    fecha_impresion = datetime.now().strftime("%d/%m/%Y %I:%M %p")

    title = Paragraph("<b>COMISARÍA PNP PICHANAQUI - SECCIÓN CUSTODIA DE DETENIDOS</b><br/><font size=9 color='black'>REPORTE OFICIAL DE PERSONAS EN CONDICIÓN DE DETENIDAS / RETENIDAS</font>", style_title)
    elements.append(title)
    elements.append(Spacer(1, 4))

    meta_info = Paragraph(f"<b>FECHA Y HORA DE IMPRESIÓN DEL REPORTE:</b> {fecha_impresion}", style_meta)
    elements.append(meta_info)
    elements.append(Spacer(1, 12))
    
    headers = [
        Paragraph("DNI / DOC", style_header),
        Paragraph("Nombres y Apellidos", style_header),
        Paragraph("Condición Legal", style_header),
        Paragraph("Motivo de Detención", style_header),
        Paragraph("Sección", style_header),
        Paragraph("Instructor PNP a Cargo", style_header),
        Paragraph("Hora Ingreso", style_header),
        Paragraph("Salida / Disposición", style_header)
    ]
    
    data = [headers]
    
    # Filtro exclusivo de Detenidos y Retenidos
    detenidos = [r for r in registros if r.get("situacion") in ["DETENIDO", "RETENIDO"]]
    
    for r in detenidos:
        estado_texto = r.get("hora_salida") if r.get("hora_salida") else "EN CUSTODIA"
        situacion_texto = r.get("situacion", "DETENIDO")
        instructor = r.get("instructor") if r.get("instructor") else "NO REGISTRADO"
        
        fila = [
            Paragraph(str(r.get("dni", "")), style_cell_bold),
            Paragraph(str(r.get("nombre", "")), style_cell_bold),
            Paragraph(f"<font color='red'><b>{situacion_texto}</b></font>", style_cell),
            Paragraph(str(r.get("motivo", "")), style_cell),
            Paragraph(str(r.get("destino", "")), style_cell),
            Paragraph(f"<b>{instructor}</b>", style_cell), # Se incluye el Instructor PNP
            Paragraph(str(r.get("hora_ingreso", "")), style_cell),
            Paragraph(f"<b>{estado_texto}</b>", style_cell)
        ]
        data.append(fila)
        
    col_widths = [65, 135, 75, 100, 90, 120, 65, 70]
    
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#8B0000")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#FFF0F0")])
    ]))
    
    elements.append(t)
    doc.build(elements)
    buffer.seek(0)
    return buffer