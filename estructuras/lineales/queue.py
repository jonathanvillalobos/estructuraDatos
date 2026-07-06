from estructuras.lineales.nodo import Node       

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, valor):
        # Agrega el valor al final de la cola
        nuevo_nodo = Node(valor)
        if self.isEmpty():
            self.first = nuevo_nodo
            self.last = nuevo_nodo
        else:
            self.last.next = nuevo_nodo 
            self.last = nuevo_nodo       
        self.size += 1

    def dequeue(self):
        # Elimina el primer elemento que entró
        if self.isEmpty():
            return None
        
        eliminado = self.first.data  # <-- Corregido: .data en lugar de .value
        self.first = self.first.next  
        
        if self.first is None:        
            self.last = None
            
        self.size -= 1
        return eliminado

    def firstQueue(self):
        # Consulta el primer elemento sin eliminarlo
        if self.isEmpty():
            return None
        return self.first.data  # <-- Corregido: .data en lugar de .value

    def lastQueue(self):
        # Consulta el último elemento sin eliminarlo
        if self.isEmpty():
            return None
        return self.last.data  # <-- Corregido: .data en lugar de .value

    def printQueue(self):
        # Devuelve el contenido completo de la cola
        if self.isEmpty():
            return "Cola vacía"
        
        elementos = []
        actual = self.first
        while actual is not None:
            elementos.append(str(actual.data))  # <-- Corregido: .data en lugar de .value
            actual = actual.next
        return " -> ".join(elementos)

    def isEmpty(self):
        return self.first == None

    def to_list(self):
        """Convierte los valores de la cola en una lista común de Python"""
        elementos = []
        actual = self.first
        while actual is not None:
            elementos.append(actual.data)  # <-- Corregido: .data en lugar de .value
            actual = actual.next
        return elementos