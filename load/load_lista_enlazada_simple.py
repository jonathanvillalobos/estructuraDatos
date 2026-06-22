from PyQt5 import QtWidgets

class LoadLinkedList:
    def __init__(self, dialog_ui, linked_list):
        self.ui = dialog_ui
        self.list = linked_list
        self.init_events()
        self.actualizar_vista_lista()

    def init_events(self):
        self.ui.pushButton.clicked.connect(self.insertar_inicio)
        self.ui.pushButton_2.clicked.connect(self.insertar_final)
        self.ui.pushButton_4.clicked.connect(self.eliminar_inicio)
        self.ui.pushButton_3.clicked.connect(self.eliminar_final)
        self.ui.pushButton_5.clicked.connect(self.buscar)

    def obtener_input(self):
        # Almacenamos el texto en una variable local ANTES de borrar el componente gráfico
        texto_capturado = str(self.ui.lineEdit.text()).strip()
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
        return texto_capturado

    def mostrar_mensaje(self, titulo, mensaje, icono=QtWidgets.QMessageBox.Information):
        msg = QtWidgets.QMessageBox(self.ui)
        msg.setIcon(icono)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.exec_()

    def actualizar_vista_lista(self):
        resultado = []
        temp = self.list.head
        while temp is not None:
            resultado.append(str(temp.data))
            temp = temp.next
        resultado.append("None (Tail)")
        texto_final = " -> ".join(resultado)
        self.ui.lblResultado.setText(texto_final)

    def insertar_inicio(self):
        dato = self.obtener_input()
        if dato:  # Verifica que no esté vacío
            self.list.insert_at_begining(dato)
            self.actualizar_vista_lista()
        else:
            self.mostrar_mensaje("Error", "El campo de datos está vacío.", QtWidgets.QMessageBox.Warning)

    def insertar_final(self):
        dato = self.obtener_input()
        if dato:
            self.list.insert_at_end(dato)
            self.actualizar_vista_lista()
        else:
            self.mostrar_mensaje("Error", "El campo de datos está vacío.", QtWidgets.QMessageBox.Warning)

    def eliminar_inicio(self):
        if self.list.head is None:
            self.mostrar_mensaje("Lista Vacía", "No hay elementos para eliminar.", QtWidgets.QMessageBox.Warning)
            return
        self.list.delete_at_begining()
        self.actualizar_vista_lista()

    def eliminar_final(self):
        if self.list.head is None:
            self.mostrar_mensaje("Lista Vacía", "No hay elementos para eliminar.", QtWidgets.QMessageBox.Warning)
            return
        self.list.delete_at_end()
        self.actualizar_vista_lista()

    def buscar(self):
        dato = self.obtener_input()
        if dato:
            encontrado = self.list.search(dato)
            if encontrado:
                self.mostrar_mensaje("Resultado de búsqueda", f"El dato '{dato}' SÍ se encuentra en la lista.")
            else:
                self.mostrar_mensaje("Resultado de búsqueda", f"El dato '{dato}' NO se encuentra en la lista.", QtWidgets.QMessageBox.Critical)
        else:
            self.mostrar_mensaje("Error", "Ingresa un dato para buscar.", QtWidgets.QMessageBox.Warning)