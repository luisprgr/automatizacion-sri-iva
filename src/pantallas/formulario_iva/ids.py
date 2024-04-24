OBLIGACION_DROPDOWN_ID = "frmFlujoDeclaracion:somObligacion_label"
OBLIGACION_DECLARACION_IVA_2011_ELEMENT_ID = "frmFlujoDeclaracion:somObligacion_1"
DIALOGO_DESCARTABLE_BUTTON_XPATH = ( 
    "// div[@id='frmFlujoDeclaracion:dialogoMensajesPersonalizados']"
    "//button[contains(@id, 'frmFlujoDeclaracion')]"
)
DATE_SELECTOR_ID = "frmFlujoDeclaracion:calPeriodo"
DATE_ELEMENT_CSS_SELECTOR = "a.button-{month}"
PERIODO_FISCAL_SIGUIENTE_BUTTON_ID = "frmFlujoDeclaracion:btnObligacionSiguiente"
DESCARTAR_BORRADOR_BUTTON_XPATH = "//button/span[contains(text(), 'Rechazar')]"

PREGUNTAS_SIGUIENTE_BUTTON_ID = "frmFlujoDeclaracion:btnPerfiladorSiguiente"

FORMULARIO_CONTENT_XPATH = "//div[@id='frmFlujoDeclaracion:pnlFormularioExtendido_content']"

SECCION_BUTTON_XPATH = (
    "//div["
    "contains(@id, 'frmFlujoDeclaracion:j_idt') and "
    "contains(@id, ':{seccion_id}:seccion') and "
    "not(contains(@id, 'seccion-tab'))]" 
)

SECCION_CONTENT_XPATH = (
    "//div["
    "contains(@id, 'frmFlujoDeclaracion:j_idt') and "
    "contains(@id, ':{seccion_id}:seccion') and "
    "contains(@id, 'seccion-tab')]" 
)

VENTAS_SECCION_BUTTON_XPATH = SECCION_BUTTON_XPATH.format(seccion_id = 2)
VENTAS_SECCION_CONTENT_XPATH = SECCION_CONTENT_XPATH.format(seccion_id = 2)

RESUMEN_IMPOSITIVO_SECCION_BUTTON_XPATH = SECCION_BUTTON_XPATH.format(seccion_id = 6)
RESUMEN_IMPOSITIVO_SECCION_CONTENT_XPATH = SECCION_CONTENT_XPATH.format(seccion_id = 6)

DEVOLUCION_ISD_SECCION_BUTTON_XPATH = SECCION_BUTTON_XPATH.format(seccion_id = 8)
DEVOLUCION_ISD_SECCION_CONTENT_XPATH = SECCION_CONTENT_XPATH.format(seccion_id = 8)

TOTALES_SECCION_BUTTON_XPATH = SECCION_BUTTON_XPATH.format(seccion_id = 12)
TOTALES_SECCION_CONTENT_XPATH = SECCION_CONTENT_XPATH.format(seccion_id = 12)

GUARDAR_BORRADOR_BUTTON_XPATH = "//button/span[contains(text(), 'Guardar borrador')]"
