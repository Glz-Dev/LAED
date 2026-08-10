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
    resultado = [ListaDupla() for _ in range(k)]

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


# Criando a lista original
lista = ListaDupla()

for valor in [1, 3, 7, 10, 13, 18, 21, 27]:
    lista.inserir_fim(valor)


# Dividir em 3 sublistas
resultado = lista_de_listas(lista, 3)


# Mostrar resultado
for i in range(len(resultado)):
    print("Lista", i + 1, ":", end=" ")
    resultado[i].imprimir()