class Nodo(object):
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def lista(lista_numeros):
    if not lista_numeros:
        return None
    mid_num = len(lista_numeros)//2
    nodo = Nodo(lista_numeros[mid_num])
    nodo.izq = lista(lista_numeros[:mid_num])
    nodo.der = lista(lista_numeros[mid_num+1:])
    return nodo

def preOrder(nodo): 
    if not nodo: 
        return      
    print(nodo.valor)
    preOrder(nodo.izq) 
    preOrder(nodo.der)   

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

print("Numeros en orden:")
print(lista_numeros)
c = lista(lista_numeros)
print("\nLista de numeros:")
print(preOrder(c))