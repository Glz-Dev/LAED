class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_fim(self, valor):
        novo = No(valor)

        if self.inicio is None:
            self.inicio = novo
            return

        atual = self.inicio

        while atual.prox:
            atual = atual.prox

        atual.prox = novo


    def imprimir(self):
        atual = self.inicio

        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.prox

        print("None")

def intercalar(l1, l2):

    resultado = ListaEncadeada()
    p1 = l1.inicio
    p2 = l2.inicio
    while p1 and p2:
        if p1.valor <= p2.valor:
            resultado.inserir_fim(p1.valor)
            p1 = p1.prox

        else:
            resultado.inserir_fim(p2.valor)
            p2 = p2.prox

    while p1:
        resultado.inserir_fim(p1.valor)
        p1 = p1.prox
    while p2:
        resultado.inserir_fim(p2.valor)
        p2 = p2.prox


    return resultado

#Complexidade O(n+m)