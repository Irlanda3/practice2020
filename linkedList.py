# https://www.youtube.com/watch?v=6sBsF13n5ig
class linkedListNode:
    """clone el repositorio de practoce2020. Entonces me pidio lugar para guardar el repositorio y lo que hice fue escojer documents
entonces hay un folder que dice practice2020. cuando abra VS code tengo que fijarme si estoy en ese directorio correcto
o si no cerrar todo y escojer en que directorio estar
"""
    def __init__(self, value, nextNode=None): #parameters
        
        self.value = value
        self.nextNode = nextNode
        
# "3" -> "7" ->"10"
node1 = linkedListNode("3")
node2 = linkedListNode("7") 
node3 = linkedListNode("10")

node1.nextNode = node2 # node1 -> node2, "3" -> "7"
node2.nextNode = node3 # node2 -> node3, "7" -> "10"

# printing nodes
currentNode = node1
while True:
    print (currentNode.value, "->") 
    if currentNode.nextNode is None: # si el siguiente node es none, sale
        print ("None")
        break
    currentNode = currentNode.nextNode
    
# Simple node class for adding nodes manually