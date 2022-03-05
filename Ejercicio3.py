class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def bst(nodo):
    stack = []
    prev = None
    
    while nodo or stack:
        while nodo:
            stack.append(nodo)
            nodo = nodo.izq
        nodo = stack.pop()
        if prev and nodo.valor <= prev.valor:
            return False
        prev = nodo
        nodo = nodo.der
    return True

nodo = Nodo(2)  
nodo.izq = Nodo(1)  
nodo.der = Nodo(3) 
 
c = bst(nodo)
print(c)

nodo = Nodo(1)  
nodo.izq = Nodo(2)  
nodo.der = Nodo(3) 
 
c = bst(nodo)
print(c)