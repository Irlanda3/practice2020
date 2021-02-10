# https://www.youtube.com/watch?v=6sBsF13n5ig
class linkedListNode:
    def __init__(self, value, nextNode=None): #parameters
        """
        docstring
        """
        self.value = value
        self.nextNode = nextNode
        
        
class linkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, value): # Create a node out of the value is passed in
        node = linkedListNode(value)
        if self.head is None: # If we do not have a node in the linked list
            self.head = node # Si el linked list esta vacio entonces el head es igual al nuevo que hemos creado.
            return # Y regresamos
        
        # If it is not the head node tenemos otro caso entonces. Look out for the head node is and try to find the tail by traversing the linkedlist using the head node
        currentNode = self.head
        while True:
            if currentNode.nextNode is None: # If there is no node after the current node we are at
                currentNode.nextNode = node # then we are going to make that next node our node
                break # Y salimos por que pusimos el nodo en el tail
            currentNode = currentNode.nextNode # If it is not the tail node solo we keep traversing. Aqui es como actualizar el currentNode
            
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.nextNode # Actulizamos el currentNode
        print("None") 
        
        
        
ll = linkedList() # we create a linkedlist
ll.printLinkedList() # Y nos imprime quee esta vacio "NONE" por que no hemos agregado nada dentro del nodo
ll.insert("3")
ll.printLinkedList()
ll.insert("44")
ll.printLinkedList()
ll.insert("55")
ll.printLinkedList()            
            
        
        
