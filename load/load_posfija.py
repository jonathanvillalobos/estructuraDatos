# load_conversion.py
import sys
from PyQt5 import QtWidgets, uic
from estructuras.aplicaciones.posfija import ExpressionConverter

class VentanaConversion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/posfija.ui', self)
        
        self.converter = ExpressionConverter()
        self.pushButton.clicked.connect(self.procesar_conversion)

    def procesar_conversion(self):
        """Lee el input, invoca la conversión y la posterior evaluación."""
        infija = self.lineEdit.text()
        
        if not infija.strip():
            self.label_2.setText("Ingresa una expresión")
            return
            
        try:
            # 1. Convertimos de infija a posfija
            posfija = self.converter.infix_to_postfix(infija)
            
            # 2. Evaluamos la expresión posfija resultante
            resultado_numerico = self.converter.evaluate_postfix(posfija)
            
            # 3. Formateamos la salida para mostrar ambos datos en la misma etiqueta 'label_2'
            # Si el resultado es entero (ej: 14.0), lo mostramos como 14
            if resultado_numerico.is_integer():
                resultado_numerico = int(resultado_numerico)
                
            texto_final = f"Posfija: {posfija}  |  Resultado: {resultado_numerico}"
            self.label_2.setText(texto_final)
            
        except ZeroDivisionError:
            self.label_2.setText("Error: División entre cero.")
        except Exception as e:
            self.label_2.setText(f"Error en la expresión.")