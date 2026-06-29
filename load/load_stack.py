from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.stack import Stack 

class LoadStack(QDialog):
    def __init__(self):
        super().__init__()
        # 1. Carga el archivo .ui de forma manual
        uic.loadUi("ui/pila.ui", self)
        
        # 2. Inicializa la estructura de datos interna
        self.pila = Stack()
        
        # 3. Enlaces directos a las funciones usando los objectNames de tu ui/pila.ui
        self.pushButton.clicked.connect(self.ejecutar_push)   # Push
        self.pushButton_2.clicked.connect(self.ejecutar_pop)  # Pop
        self.pushButton_3.clicked.connect(self.ejecutar_top)  # Top
        self.pushButton_4.clicked.connect(self.mostrar_pila)  # Print

    def ejecutar_push(self):
        data = self.lineEdit.text().strip()
        if data:
            self.pila.push(data)
            self.lineEdit.clear()
            self.mostrar_pila()
            self.lineEdit.setFocus()
        else:
            self.lineEdit_2.setText("¡Escribe un dato primero!")

    def ejecutar_pop(self):
        if self.pila.pop() is not None:
            self.mostrar_pila()
        else:
            self.lineEdit_2.setText("Error: La pila ya está vacía")

    def ejecutar_top(self):
        cima = self.pila.top()
        self.lineEdit_2.setText(f"Cima (Top): {cima}" if cima else "Pila vacía")

    def mostrar_pila(self):
        if self.pila.is_empty():
            self.lineEdit_2.setText("Pila Vacía")
            return
        
        nodos = []
        actual = self.pila.head
        while actual:
            nodos.append(str(actual.data))
            actual = actual.next
        
        self.lineEdit_2.setText("Top -> " + " -> ".join(nodos) + " -> Base")