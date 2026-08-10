class No:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        
def trocar(lista, a, b):
    if a.prox != b:
        return

    antes = a.ant
    depois = b.prox

    if antes is not None:
        antes.prox = b
    else:
        lista.inicio = b

    if depois is not None:
        depois.ant = a
    else:
        lista.fim = a

    b.ant = antes
    b.prox = a

    a.ant = b
    a.prox = depois
def varredura(lista):
    atual = lista.inicio

    while atual is not None and atual.prox is not None:

        proximo = atual.prox

        if atual.valor > proximo.valor:
            trocar(lista, atual, proximo)
            atual = atual.prox
        else:
            atual = atual.prox