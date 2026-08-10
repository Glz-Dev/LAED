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


def maior_no_fim(lista):

    if lista.inicio is None:
        return

    maior = lista.inicio
    anterior_maior = None
    anterior = None
    atual = lista.inicio


    while atual:
        if atual.valor > maior.valor:
            maior = atual
            anterior_maior = anterior

        anterior = atual
        atual = atual.prox

    # já está no final
    if maior.prox is None:
        return


    # remover o maior
    if anterior_maior:
        anterior_maior.prox = maior.prox
    else:
        lista.inicio = maior.prox


    # colocar no final
    atual = lista.inicio

    while atual.prox:
        atual = atual.prox

    atual.prox = maior
    maior.prox = None

    #O(n)