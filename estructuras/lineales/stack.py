from estructuras.lineales.nodo import Node

class Stack(object):
    def __init__(self):
        self.head = None  # Representa el 'Top' de la pila

    def is_empty(self):
        return self.head is None 
    
    def push(self, data):
        """Inserta un elemento en la parte superior (Top)"""
        nuevo_nodo = Node(data)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    def pop(self):
        """Elimina y retorna el elemento en la parte superior (Top)"""
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def top(self):
        return self.head.data if self.head else None

    def print_stack(self):
        if not self.head:
            print("Stack: Empty")
            return
        
        nodos = []
        actual = self.head
        while actual:
            nodos.append(str(actual.data))
            actual = actual.next
        
        print("Top -> " + " -> ".join(nodos) + " -> Base")

   