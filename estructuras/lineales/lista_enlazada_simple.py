from estructuras.lineales.nodo import Node 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_begining(self, data):
        #Paso 1: Crear unnuevo nodo con el dato proporcionado
        new_node =Node(data)
        
        #Paso 2: Verificar si la lista esta vacia 
        if self.head is None:
            #Si la lista esta vacia, el nuevo nodo se convierte en la cabeza y la cola 
            self.head = new_node 
            self.tail - new_node
        else:
            #Si la lista no esta vacia, el nuevo nodo apunta a la cabeza actual
            new_node.next = self.head
            #Luego, la cabeza se actualiza para ser el nuevo nodo 
            self.head = new_node 
            
    def print_Linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "->", end="")
            temp = temp.next
        print("<- Tail")
            

            
        
        
        