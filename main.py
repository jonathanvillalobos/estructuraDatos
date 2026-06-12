from estructuras.lineales.lista_enlazada_simple import LinkedList

def main():
    lista = LinkedList()
    lista.insert_at_begining(10)
    lista.insert_at_begining(20)
    lista.insert_at_begining(30)
    lista.print_linked_list()
    
    if __name__ == "__main__":
        main()