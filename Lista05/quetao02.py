class No:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
def elemento_central(lista):
    if lista.inicio is None:
        return None

    esquerda = lista.inicio
    direita = lista.fim

    while esquerda != direita and esquerda.prox != direita:
        esquerda = esquerda.prox
        direita = direita.ant

    return esquerda.valor