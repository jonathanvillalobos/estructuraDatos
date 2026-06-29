from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.lista_enlazada_simple import LinkedList

class LoadLinkedList(QDialog):
    def __init__(self):
        super().__init__()
        # 1. Carga el archivo .ui de forma manual para esta ventana
        uic.loadUi("ui/listan enlazada.ui", self)
        
        # 2. Crea el objeto de tu clase LinkedList de forma interna
        self.list = LinkedList()
        
        # 3. Enlaces directos a las funciones usando los objectNames de tu UI
        self.pushButton.clicked.connect(self.insertar_inicio)   # Botón Insertar Inicio
        self.pushButton_2.clicked.connect(self.insertar_final)  # Botón Insertar Final
        self.pushButton_4.clicked.connect(self.eliminar_inicio) # Botón Eliminar Inicio
        self.pushButton_3.clicked.connect(self.eliminar_final)  # Botón Eliminar Final
        self.pushButton_5.clicked.connect(self.buscar)          # Botón Buscar

    def obtener_input(self):
        # Captura el texto, limpia la casilla gráfica y regresa la data limpia
        texto_capturado = str(self.lineEdit.text()).strip()
        self.lineEdit.clear()
        self.lineEdit.setFocus()
        return texto_capturado

    def actualizar_vista_lista(self):
        # Si la lista está vacía, lo muestra directamente en la etiqueta de resultado
        if self.list.head is None:
            self.lblResultado.setText("Lista Vacía -> None (Tail)")
            return
            
        resultado = []
        temp = self.list.head
        while temp is not None:
            resultado.append(str(temp.data))  # <--- Usando .data del nodo
            temp = temp.next
        resultado.append("None (Tail)")
        
        # Actualiza el componente de texto en la interfaz (lblResultado)
        self.lblResultado.setText(" -> ".join(resultado))

    def insertar_inicio(self):
        data = self.obtener_input()  # <--- Cambiado de 'dato' a 'data'
        if data:
            self.list.insert_at_begining(data)
            self.actualizar_vista_lista()
        else:
            self.lblResultado.setText("¡Escribe una data primero!")

    def insertar_final(self):
        data = self.obtener_input()  # <--- Cambiado de 'dato' a 'data'
        if data:
            self.list.insert_at_end(data)
            self.actualizar_vista_lista()
        else:
            self.lblResultado.setText("¡Escribe una data primero!")

    def eliminar_inicio(self):
        if self.list.head is None:
            self.lblResultado.setText("Error: La lista ya está vacía")
            return
        self.list.delete_at_begining()
        self.actualizar_vista_lista()

    def eliminar_final(self):
        if self.list.head is None:
            self.lblResultado.setText("Error: La lista ya está vacía")
            return
        self.list.delete_at_end()
        self.actualizar_vista_lista()

    def buscar(self):
        data = self.obtener_input()  # <--- Cambiado de 'dato' a 'data'
        if data:
            encontrado = self.list.search(data)
            if encontrado:
                self.lblResultado.setText(f"Resultado: La data '{data}' SÍ se encuentra en la lista.")
            else:
                self.lblResultado.setText(f"Resultado: La data '{data}' NO se encuentra en la lista.")
        else:
            self.lblResultado.setText("¡Ingresa una data para buscar!")