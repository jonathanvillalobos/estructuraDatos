# main.py
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.aplicaciones.impresora import ControladorFIFO

class VentanaColaImpresion(QDialog):
    def __init__(self):
        super().__init__()
        
        # 1. Cargar la interfaz gráfica desde el archivo .ui de QtDesigner
        uic.loadUi("ui/impresora.ui", self)
        
        # 2. Instanciar nuestro controlador (el cerebro FIFO)
        self.controlador = ControladorFIFO()
        
        # 3. Conectar los eventos de los botones con los métodos de esta clase
        self.btn_agregar.clicked.connect(self.action_agregar)
        self.btn_imprimir.clicked.connect(self.action_procesar)
        
        # 4. Actualizar el estado visual inicial
        self.actualizar_vista()

    # ==========================================
    # MÉTODOS DE ACCIÓN (CONEXIÓN CON EL BOTÓN)
    # ==========================================

    def action_agregar(self):
        """Acción al presionar el botón 'Agregar a la Cola'."""
        # Obtener los datos directamente de los inputs de la interfaz
        usuario = self.txt_usuario.text()
        documento = self.txt_documento.text()
        paginas = self.spin_paginas.value()

        # Enviar los datos al controlador para que los valide y los encole
        exito, mensaje = self.controlador.agregar_trabajo(usuario, documento, paginas)

        if exito:
            # Si se agregó con éxito, limpiamos los campos para el siguiente ingreso
            self.txt_usuario.clear()
            self.txt_documento.clear()
            self.spin_paginas.setValue(1)
            # Enfocamos de nuevo el primer campo para comodidad del usuario
            self.txt_usuario.setFocus()
            
            # Actualizamos la pantalla
            self.actualizar_vista()
        else:
            # Si falló la validación, mostramos la alerta de error en pantalla
            QMessageBox.warning(self, "Validación de Entrada", mensaje)

    def action_procesar(self):
        """Acción al presionar el botón 'Imprimir Siguiente'."""
        # Intentamos retirar el elemento del frente a través del controlador
        trabajo, mensaje = self.controlador.procesar_siguiente()

        if trabajo is not None:
            # Si había un trabajo, mostramos un mensaje de éxito detallando qué se atendió
            QMessageBox.information(
                self, 
                "Procesando Documento", 
                f"🖨️ Se atendió exitosamente el siguiente trabajo:\n\n"
                f"• Documento: {trabajo.documento}\n"
                f"• Solicitado por: {trabajo.usuario}\n"
                f"• Páginas: {trabajo.paginas}"
            )
            # Actualizamos la pantalla para reflejar el cambio
            self.actualizar_vista()
        else:
            # Si la cola estaba vacía, el controlador avisa y mandamos una advertencia
            QMessageBox.information(self, "Cola Vacía", mensaje)


    # ==========================================
    # MÉTODO DE ACTUALIZACIÓN VISUAL (SINCRO)
    # ==========================================

    def actualizar_vista(self):
        """Sincroniza todos los widgets de la interfaz con los datos del controlador."""
        
        # 1. ACTUALIZAR CONSULTA: Mostrar todos los trabajos pendientes en su orden actual
        self.list_visual.clear()
        trabajos_pendientes = self.controlador.obtener_pendientes()
        
        for i, trabajo in enumerate(trabajos_pendientes, start=1):
            # Agregamos cada objeto de impresión al QListWidget usando su método __str__
            self.list_visual.addItem(f"{i}. {trabajo}")

        # 2. ACTUALIZAR ESTADO: Cantidad de trabajos pendientes
        total = self.controlador.obtener_total_pendientes()
        self.lbl_total_pendientes.setText(f"Trabajos pendientes en cola: {total}")

        # 3. ACTUALIZAR ESTADO: Elemento que está al frente (Peek) sin retirarlo
        siguiente = self.controlador.obtener_siguiente_en_espera()
        if siguiente:
            self.lbl_siguiente.setText(
                f"Siguiente en la cola:\n📄 {siguiente.documento} (por {siguiente.usuario})"
            )
        else:
            self.lbl_siguiente.setText("Siguiente en la cola: Ninguno")

