class LoadMenu:
    def __init__(self, main_window_ui, dialog_class):
        self.ui = main_window_ui
        self.dialog_class = dialog_class
        self.init_events()

    def init_events(self):
        self.ui.actionLista_enlazada.triggered.connect(self.abrir_lista_enlazada)

    def abrir_lista_enlazada(self):
        dialogo = self.dialog_class()
        dialogo.exec_()