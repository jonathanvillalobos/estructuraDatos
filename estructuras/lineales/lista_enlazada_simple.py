from estructuras.lineales.nodo import Node 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node  
        else:
            new_node.next = self.head
            self.head = new_node 
            
    def print_Linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None (Tail)")
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # Cambiado a una validación directa y limpia
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def delete_at_begining(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
     
    def delete_at_end(self):
        if not self.head: 
            return
        if self.head == self.tail: 
            self.head = None
            self.tail = None
            return
            
        actual = self.head
        while actual.next.next is not None:
            actual = actual.next
        
        actual.next = None 
        self.tail = actual 
              
    def search(self, data):
        current_node = self.head
        while current_node:
            if str(current_node.data) == str(data): # Forzamos comparación de strings
                return True 
            current_node = current_node.next
        return False
            

            
        
        
        