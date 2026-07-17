# load_banco.py
from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic

# Importación directa del controlador
from estructuras.aplicaciones.banco import ControladorBanco

class SistemaBanco(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/banco.ui", self)
        
        self.controlador = ControladorBanco()
        
        # --- CONEXIÓN DE BOTONES ---
        self.pushButton.clicked.connect(self.click_turno)       
        self.pushButton_2.clicked.connect(self.click_atender)   
        self.pushButton_3.clicked.connect(self.click_cerrar)    

    def click_turno(self):
        nuevo_turno = self.controlador.registrar_nuevo_turno()
        if nuevo_turno:
            self.lineEdit.setText(str(nuevo_turno))
            self.label_4.setText("") 
            hora_registro = datetime.now().strftime("%H:%M:%S")
            
            # Agrega el turno y su hora de recogida al listWidget de inmediato
            self.listWidget.addItem(f"T#{nuevo_turno} - Llegada: {hora_registro}") 

    def click_atender(self):
        resultado = self.controlador.procesar_atencion()
        
        if resultado is None:
            self.label_4.setText("No hay turnos.")
            return
            
        # --- NUEVO FORMATO DE TEXTO ---
        # "resultado" contiene: "numero", "hora_atencion" y "tiempo_transcurrido"
        texto_pantalla = f"T#{resultado['numero']} | Atendido: {resultado['hora_atencion']} | Esperó: {resultado['tiempo_transcurrido']}"
        
        # Mostramos toda la cadena en el lineEdit_2
        self.lineEdit_2.setText(texto_pantalla)
        self.label_4.setText("Atendiendo...")
        
        # Remover el primer elemento del listWidget (FIFO)
        if self.listWidget.count() > 0:
            item_atendido = self.listWidget.takeItem(0)
            del item_atendido 
        
        # Verificar si el banco ya cerró y no hay nadie más en cola
        if self.controlador.banco_cerrado and self.controlador.cola_espera.isEmpty():
            self.mostrar_resultados_en_pantalla()
            
    def click_cerrar(self):
        self.pushButton.setEnabled(False)
        turnos_restantes = self.controlador.intentar_cierre()
        
        if turnos_restantes > 0:
            self.label_4.setText("Esperando turnos")
        else:
            self.mostrar_resultados_en_pantalla()

    def mostrar_resultados_en_pantalla(self):
        metricas = self.controlador.obtener_metricas_finales()
        
        self.label_4.setText("Finalizado")
        self.lineEdit_3.setText(metricas["total_atendidos"])
        self.lineEdit_4.setText(metricas["tiempo_promedio"])
        
        QMessageBox.information(self, "Cierre de Caja", "Todos los clientes han sido atendidos con éxito.")

