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


def atualizar(lista, x, y):

    
    atual = lista.inicio

    while atual is not None and atual.valor != x:
        atual = atual.prox

    if atual is None:
        return False

   

    if atual.ant is not None:
        atual.ant.prox = atual.prox
    else:
        lista.inicio = atual.prox

    if atual.prox is not None:
        atual.prox.ant = atual.ant
    else:
        lista.fim = atual.ant

    atual.ant = None
    atual.prox = None

    
    atual.valor = y

    
    p = lista.inicio

    while p is not None and p.valor < y:
        p = p.prox

    
    if lista.inicio is None:

        lista.inicio = atual
        lista.fim = atual

    
    elif p is None:

        atual.ant = lista.fim
        lista.fim.prox = atual
        lista.fim = atual

    
    elif p == lista.inicio:

        atual.prox = lista.inicio
        lista.inicio.ant = atual
        lista.inicio = atual

    
    else:

        atual.ant = p.ant
        atual.prox = p

        p.ant.prox = atual
        p.ant = atual

    return True




lista = ListaDupla()

lista.inserir_fim(3)
lista.inserir_fim(5)
lista.inserir_fim(9)
lista.inserir_fim(10)
lista.inserir_fim(15)

print("Antes:")
lista.imprimir()

atualizar(lista, 9, 14)

print("Depois de atualizar 9 para 14:")
lista.imprimir()