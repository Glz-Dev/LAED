class No:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_fim(self, valor):
        novo = No(valor)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.ant = self.fim
            self.fim.prox = novo
            self.fim = novo

    def imprimir(self):
        atual = self.inicio

        while atual is not None:
            print(atual.valor, end=" ")
            atual = atual.prox

        print()


def elemento_central(lista):

    if lista.inicio is None:
        return None

    esquerda = lista.inicio
    direita = lista.fim

    while esquerda != direita and esquerda.prox != direita:
        esquerda = esquerda.prox
        direita = direita.ant

    return esquerda.valor


#