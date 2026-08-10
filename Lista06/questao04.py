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


def particionar(lista, k):

    q = lista.inicio
    r = lista.fim

    while q is not None and r is not None:

       
        while q is not None and q.valor <= k:
            q = q.prox

        
        while r is not None and r.valor > k:
            r = r.ant

        if q is None or r is None:
            break

        if q == r:
            break

       
        q.valor, r.valor = r.valor, q.valor

        q = q.prox
        r = r.ant

