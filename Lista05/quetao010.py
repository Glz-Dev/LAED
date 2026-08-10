def busca(L, x):
    for lista in L:

        if lista.inicio is None:
            continue

        if x < lista.inicio.valor:
            return None

        if x <= lista.fim.valor:

            atual = lista.inicio

            while atual is not None:

                if atual.valor == x:
                    return atual

                if atual.valor > x:
                    return None

                atual = atual.prox

            return None

    return None
def busca(L, x):
    for lista in L:

        if lista.inicio is None:
            continue

        if x < lista.inicio.valor:
            return None

        if x <= lista.fim.valor:

            atual = lista.inicio

            while atual is not None:

                if atual.valor == x:
                    return atual

                if atual.valor > x:
                    return None

                atual = atual.prox

            return None

    return None
def remocao(L, x):

    no = busca(L, x)

    if no is None:
        return False

    for lista in L:

        atual = lista.inicio

        while atual is not None:

            if atual == no:

                if atual.ant is not None:
                    atual.ant.prox = atual.prox
                else:
                    lista.inicio = atual.prox

                if atual.prox is not None:
                    atual.prox.ant = atual.ant
                else:
                    lista.fim = atual.ant

                return True

            atual = atual.prox

    return False