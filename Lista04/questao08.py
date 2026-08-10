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

def elemento_mais_frequente(lista):

    maior = 0
    resposta = None
    atual = lista.inicio


    while atual:
        contador = 0
        outro = lista.inicio
        while outro:
            if atual.valor == outro.valor:
                contador += 1
            outro = outro.prox
        if contador > maior:
            maior = contador
            resposta = atual.valor
        atual = atual.prox
    return resposta, maior

#Complexidade O(n²)

