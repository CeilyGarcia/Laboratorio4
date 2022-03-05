class Nodo(object):
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def pequeño(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.izq
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.der
    return root.valor

root = Nodo(20)  
root.izq = Nodo(11)  
root.der = Nodo(18) 
root.izq.izq = Nodo(8)  
root.izq.der = Nodo(12) 
root.izq.der.izq = Nodo(5)  
root.izq.der.der = Nodo(9)  
root.der.der = Nodo(20) 
root.der.der.izq = Nodo(22)  

print(pequeño(root, 2))
print(pequeño(root, 3))