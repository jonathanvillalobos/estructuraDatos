# load_conversion.py
import sys
from PyQt5 import QtWidgets, uic
# Importamos la lógica que creamos previamente
from estructuras.aplicaciones.posfija import ExpressionConverter

class VentanaConversion(QtWidgets.QDialog): # <-- Cambiado a QDialog para coincidir con tu .ui
    def __init__(self):
        # 1. Inicializa el constructor padre de QDialog
        super().__init__()
        
        # 2. Carga los componentes del archivo .ui directamente
        # Cambia 'tu_diseño.ui' por el nombre real de tu archivo de Qt Designer
        uic.loadUi('ui/posfija.ui', self)
        
        # 3. Instancia de la lógica orientada a objetos (La Pila)
        self.converter = ExpressionConverter()
        
        # 4. Conectamos el botón usando su nombre exacto del XML: 'pushButton'
        self.pushButton.clicked.connect(self.procesar_conversion)

    def procesar_conversion(self):
        """Lee el input del 'lineEdit', invoca la pila y muestra el resultado en 'label_2'."""
        # Recuperamos la expresión infija usando el name real
        infija = self.lineEdit.text()
        
        # Validación básica por si el campo está vacío
        if not infija.strip():
            self.label_2.setText("Ingresa una expresión")
            return
            
        # Ejecutamos la conversión que utiliza la estructura Stack
        posfija = self.converter.infix_to_postfix(infija)
        
        # Mostramos la conversión en la etiqueta real asignada por Qt: 'label_2'
        self.label_2.setText(posfija)