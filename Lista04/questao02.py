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

def separar(lista):
    pares = ListaEncadeada()
    impares = ListaEncadeada()
    atual = lista.inicio


    while atual:
        if atual.valor % 2 == 0:
            pares.inserir_fim(atual.valor)
        else:
            impares.inserir_fim(atual.valor)

        atual = atual.prox
    return pares, impares

#Complexidade O(n)