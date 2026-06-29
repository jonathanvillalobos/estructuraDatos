import sys
from PyQt5.QtWidgets import QApplication
# Importamos tu clase LoadMenu desde su archivo correspondiente
from load.load_menu import LoadMenu

def main():
    # 1. Inicializamos la aplicación de PyQt5
    app = QApplication(sys.argv)
    
    # 2. Instanciamos el menú principal (tu clase con super().__init__())
    menu = LoadMenu()
    
    # 3. Mostramos el menú en pantalla
    menu.show()
    
    # 4. Arrancamos el bucle de eventos de la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()