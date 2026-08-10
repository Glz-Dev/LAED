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


def inverter(lista):
    anterior = None
    atual = lista.inicio
    while atual:

        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo
    lista.inicio = anterior

   # Complexidade O(n)