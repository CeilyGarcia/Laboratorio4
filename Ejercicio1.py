class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self, valor):
        self.raiz = Nodo(valor)

    def agregarNodo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self.agregarNodo(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self.agregarNodo(nodo.der, valor)

    def ascendente(self, nodo):
        if nodo is not None:
            self.ascendente(nodo.izq)
            print(nodo.valor)
            self.ascendente(nodo.der)

    def buscar_nodo(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.valor == busqueda:
            return nodo
        if busqueda < nodo.valor:
            return self.buscar_nodo(nodo.izq, busqueda)
        else:
            return self.buscar_nodo(nodo.der, busqueda)

    def agregar(self, valor):
        self.agregarNodo(self.raiz, valor)

    def inorden(self):
        print("Imprimir arbol en forma ascendente: ")
        self.ascendente(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.buscar_nodo(self.raiz, busqueda)
        
arbol = Arbol("4")
arbol.agregar("1")
arbol.agregar("2")
arbol.agregar("3")
arbol.agregar("5")
arbol.agregar("6")
arbol.agregar("7")
arbol.inorden()
busqueda = input("Busca algo en el árbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")