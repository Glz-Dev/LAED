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
                "Posição:", atual.posicao
            )

            atual = atual.prox


def construir_esparso(vetor):

    lista = VetorEsparso()

    for i in range(len(vetor)):

        if vetor[i] != 0:

            lista.inserir(vetor[i], i)

    return lista

