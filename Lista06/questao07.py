
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


def tamanho(lista):

    contador = 0

    atual = lista.inicio

    while atual is not None:

        contador += 1

        atual = atual.prox

    return contador


def lista_de_listas(lista, k):

   
    resultado = []

    for i in range(k):
        resultado.append(ListaDupla())

    
    n = tamanho(lista)

    
    tamanho_base = n // k

    
    resto = n % k

    atual = lista.inicio

    
    for i in range(k):

        quantidade = tamanho_base

        
        if i < resto:
            quantidade += 1

        
        for j in range(quantidade):

            if atual is not None:

                resultado[i].inserir_fim(atual.valor)

                atual = atual.prox

    return resultado


#