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

def remover_todos(lista,k):
    while lista.inicio and lista.inicio.valor == k:
        lista.inicio = lista.inicio.prox



    atual = lista.inicio
    while atual and atual.prox:
        if atual.prox.valor == k:
            atual.prox = atual.prox.prox
        else:
            atual = atual.prox

#Complexidade O(n)