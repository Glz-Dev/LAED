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

def duplicar_impares(lista):

    atual = lista.inicio
    while atual:
        if atual.valor % 2 != 0:
            novo = No(atual.valor)
            novo.prox = atual.prox
            atual.prox = novo
            atual = novo.prox

        else:
            atual = atual.prox

#Complexidade o(n)