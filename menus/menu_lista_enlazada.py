from estructuras.lineales.lista_enlazada_simple import LinkedList
class MenuListaEnlazada(object):
    def __init__(self):
       self.lista_enlazada = LinkedList()
       
    def mostrar_menu (self):
        print("**Lista enlazada**")
        print("1. Insertar inicio")
        print("2. Insertar final")
        print("3. Buscar")
        print("4. Imprimir")
        print("5. Salir")
        
    def ejecutar_opcion(self,opcion):
       
         if opcion == 1:
            dato = input("Ingresa un dato al inicio: ")
            self.lista_enlazada.insert_at_begining(dato)
            
         elif opcion == "2":
            dato = input("Ingrese dato al final: ")
            self.lista_enlazada.insert_at_end(dato)

         elif opcion == "3":
            dato = input("Dato a buscar: ")
            
            if self.lista_enlazada.search(dato):
                print("Dato encontrado")
            else:
                print("Dato no encontrado")

         elif opcion == "4":
             self.lista_enlazada.print_linked_list()
             
         elif opcion == "5":
             print ("Saliendo del programa...")
         
         else:
            print ("Opcion no valida. Por favor, ingresa una opcion valida.")
            
    def iniciar(self):
        while True:
            self.mostrar_menu
            try:
                opcion = input("Seleccione una opcion :")
                if opcion == 5:
                    self.ejecutar_opcion(opcion)
                    break
                self.ejecutar_opcion(opcion)
            except ValueError:
                print("Entrada no valida, ingresa un numero")
             

        