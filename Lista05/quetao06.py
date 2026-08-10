class No:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

def busca_por_indice(lista, k):
    atual = lista.inicio

    while atual is not None:
        if atual.posicao == k:
            return atual.valor

        atual = atual.prox

    return 0
def busca_por_valor(lista, x):
    atual = lista.inicio

    while atual is not None:
        if atual.valor == x:
            return atual.posicao

        atual = atual.prox

    return -1
def atualizacao(lista, x, k):
    atual = lista.inicio

    while atual is not None:

        if atual.posicao == k:
            atual.valor = x
            return

        atual = atual.prox

    if x != 0:
        lista.inserir(x, k)