from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5 import uic

# Importamos las clases de carga autónomas que creamos con super().__init__()
from load.load_lista_enlazada_simple import LoadLinkedList
from load.load_stack import LoadStack
from load.load_posfija import VentanaConversion

class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Carga el archivo ui/menu.ui de forma manual
        uic.loadUi("ui/menu.ui", self)
        
        # 2. Creamos y agregamos dinámicamente la opción de la Pila al menú "Lineales"
        # Esto evita errores si aún no la habías arrastrado en Qt Designer
        self.actionPila = QAction("Pila (Stack)", self)
        self.menuLineales.addAction(self.actionPila)
        
        # 3. Inicializa las conexiones
        self.init_events()

    def init_events(self):
        # Enlace de la lista enlazada (viene desde tu XML)
        self.actionLista_enlazada.triggered.connect(self.abrir_lista_enlazada)
        
        self.actionPosfija.triggered.connect(self.abrir_posfija)
        
        # Enlace de la pila (creada dinámicamente arriba)
        self.actionPila.triggered.connect(self.abrir_pila)

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