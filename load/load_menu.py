from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5 import uic

# Importamos las clases de carga autónomas que creamos con super().__init__()
from load.load_lista_enlazada_simple import LoadLinkedList
from load.load_stack import LoadStack
from load.load_posfija import VentanaConversion
from load.load_queue import QueueApp
from load.load_banco import SistemaBanco
from load.load_impresora import VentanaColaImpresion

class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Carga el archivo ui/menu.ui de forma manual
        uic.loadUi("ui/menu.ui", self)
        
    
        
        # 2. Inicializa las conexiones
        self.init_events()

    def init_events(self):
        # Enlace de la lista enlazada (viene desde tu XML)
        self.actionLista_enlazada.triggered.connect(self.abrir_lista_enlazada)
        
        self.actionPosfija.triggered.connect(self.abrir_posfija)
        
        # Enlace de la pila (creada dinámicamente arriba)
        self.actionPila.triggered.connect(self.abrir_pila)
        
        self.actionCola.triggered.connect(self.abrir_cola)
        
        self.actionBanco.triggered.connect(self.abrir_banco)
        
        self.actionImpresora.triggered.connect(self.abrir_impresora)
        
    def abrir_banco(self):
        # Instancia autónoma con super().__init__()
        dialogo = SistemaBanco()
        dialogo.exec_()
    
    def abrir_impresora(self):
        # Instancia autónoma con super().__init__()
        dialogo = VentanaColaImpresion()
        dialogo.exec_()

    def abrir_lista_enlazada(self):
        # Instancia autónoma con super().__init__()
        dialogo = LoadLinkedList()
        dialogo.exec_()

    def abrir_pila(self):
        # Instancia autónoma con super().__init__()
        dialogo = LoadStack()
        dialogo.exec_()
        
    def abrir_posfija(self):
        """Instancia autónoma con super().__init__() para el convertidor."""
        dialogo = VentanaConversion()
        dialogo.exec_()
        
    def abrir_cola(self):
        dialogo = QueueApp()
        dialogo.exec_()