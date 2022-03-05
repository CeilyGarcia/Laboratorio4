class Nodo(object):
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def closest_value(root, target):
    a = root.valor
    numero = root.izq if target < a else root.der
    if not numero:
        return a
    b = closest_value(numero, target)
    return min((a,b), key=lambda x: abs(target-x))

root = Nodo(4)  
root.izq = Nodo(2)  
root.der = Nodo(6) 
root.izq.izq = Nodo(1)  
root.izq.der = Nodo(3) 
root.izq.der.izq = Nodo(5)  
root.izq.der.der = Nodo(7)  

c = closest_value(root, 5)
print("El numero mas cercano es: ",c)