class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None


class ListaDupla:

    def __init__(self):
        self.inicio = None
        self.fim = None


    def inserir_fim(self, valor):

        novo = NoDuplo(valor)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            return


        novo.ant = self.fim
        self.fim.prox = novo
        self.fim = novo


    def imprimir(self):

        atual = self.inicio

        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.prox

        print("None")

def elemento_central(lista):

    lento = lista.inicio
    rapido = lista.inicio
    while rapido.prox and rapido.prox.prox:
        lento = lento.prox
        rapido = rapido.prox.prox
    return lento.valor