class NoEsparso:
    def __init__(self, valor, posicao):
        self.valor = valor
        self.posicao = posicao
        self.ant = None
        self.prox = None


class VetorEsparso:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, valor, posicao):

        novo = NoEsparso(valor, posicao)

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

            print(
                "Valor:", atual.valor,
                "| Posição:", atual.posicao
            )

            atual = atual.prox



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

          
            if x == 0:

                if atual.ant is not None:
                    atual.ant.prox = atual.prox
                else:
                    lista.inicio = atual.prox

                if atual.prox is not None:
                    atual.prox.ant = atual.ant
                else:
                    lista.fim = atual.ant

            else:

                atual.valor = x

            return

        atual = atual.prox

   
    if x != 0:

        lista.inserir(x, k)

