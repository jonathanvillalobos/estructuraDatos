from estructuras.lineales.queue import Queue 

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic  # Herramienta nativa de PyQt5 para cargar archivos .ui

class QueueApp(QDialog):
    def __init__(self):
        super().__init__()
        
       # En PyQt5 cargamos el archivo .ui directamente sobre 'self'
        uic.loadUi("ui/Queue.ui", self)
        
        # Inicializar la estructura Queue
        self.cola = Queue()
        
        # En PyQt5 accedes a los botones directamente desde 'self' (sin usar self.ui)
        self.pushButton.clicked.connect(self.metodo_enqueue)
        self.pushButton_2.clicked.connect(self.metodo_dequeue)
        self.pushButton_3.clicked.connect(self.metodo_first)
        self.pushButton_4.clicked.connect(self.metodo_last)
        self.pushButton_5.clicked.connect(self.metodo_print)
        
        # Estado inicial
        self.label_2.setText("Esperando datos...")

    def metodo_enqueue(self):
        # Extraemos el texto del nuevo lineEdit limpiando espacios extra
        texto_ingresado = self.lineEdit.text().strip()
        
        if texto_ingresado:
            # Agregamos el valor real ingresado a la cola
            self.cola.enqueue(texto_ingresado)
            self.label_2.setText(f"Añadido: {texto_ingresado}")
            
            # Limpiamos el espacio de escritura para el siguiente dato
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        else:
            # Si intentan enviar un campo vacío
            self.label_2.setText("Por favor, escribe algo primero.")
            
    

    def metodo_dequeue(self):
        eliminado = self.cola.dequeue()
        if eliminado is not None:
            self.label_2.setText(f"Removido: {eliminado}")
        else:
            self.label_2.setText("Error: La cola está vacía")

    def metodo_first(self):
        primero = self.cola.firstQueue()
        if primero is not None:
            self.label_2.setText(f"Primero en fila: {primero}")
        else:
            self.label_2.setText("Ninguno (Cola vacía)")

    def metodo_last(self):
        ultimo = self.cola.lastQueue()
        if ultimo is not None:
            self.label_2.setText(f"Último en fila: {ultimo}")
        else:
            self.label_2.setText("Ninguno (Cola vacía)")

    def metodo_print(self):
        contenido = self.cola.printQueue()
        if contenido and contenido != "Cola vacía":
            self.label_2.setText(contenido)
        else:
            self.label_2.setText("Cola vacía")