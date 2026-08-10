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

def intersecao(l1,l2):
    resultado = ListaEncadeada()
    atual = l1.inicio
    while atual:
        aux = l2.inicio
        while aux:
            if atual.valor == aux.valor:
                resultado.inserir_fim(atual.valor)
                break
            aux = aux.prox
        atual = atual.prox
    return resultado

#O(n²)