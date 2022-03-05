class Nodo(object):
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def borrar(root, key):
	if not root: 
		return root
	if root.valor > key: 
		root.izq = borrar(root.izq, key)
	elif root.valor < key: 
		root.der= borrar(root.der, key)
	else: 
		if not root.der:
			return root.izq
		if not root.izq:
			return root.der
		temp_val = root.der
		mini_val = temp_val.valor
		while temp_val.izq:
			temp_val = temp_val.izq
			mini_val = temp_val.valor
		root.der = borrar(root.der,root.valor)
	return root

def preorder(nodo): 
    if not nodo: 
        return      
    print(nodo.valor)
    preorder(nodo.izq) 
    preorder(nodo.der)   
    
root = Nodo(4)  
root.izq = Nodo(2)  
root.der = Nodo(5) 
root.izq.izq = Nodo(1)  
root.izq.der = Nodo(3) 
root.izq.der.izq = Nodo(8)  
print("Principal:")
print(preorder(root))
c = borrar(root, 3)
print("Nodos eliminados:")
print(preorder(c))