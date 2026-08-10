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

def possui_repetido(lista):

    atual = lista.inicio
    while atual:
        outro = atual.prox
        while outro:
            if atual.valor == outro.valor:
                return True
            outro = outro.prox
        atual = atual.prox
    return False

#Complexidade O(n²)