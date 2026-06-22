import sys
from PyQt5 import QtWidgets, uic
from estructuras.lineales.lista_enlazada_simple import LinkedList
from load.load_lista_enlazada_simple import LoadLinkedList

class ListaDialog(QtWidgets.QDialog):
    def __init__(self, lista_existente):
        super().__init__()
        uic.loadUi("ui/listan enlazada.ui", self)
        # Usamos la lista que ya contiene los datos guardados
        self.lista_enlazada = lista_existente
        self.controlador = LoadLinkedList(self, self.lista_enlazada)

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/menu.ui", self)
        # La lista nace aquí de manera global para la aplicación
        self.lista_compartida = LinkedList()
        self.actionLista_enlazada.triggered.connect(self.abrir_lista_enlazada)

    def abrir_lista_enlazada(self):
        # Le pasamos la lista de la ventana principal al diálogo
        dialogo = ListaDialog(self.lista_compartida)
        dialogo.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())