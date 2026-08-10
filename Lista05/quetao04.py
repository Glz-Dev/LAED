class No:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

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
        
        p = q
        encontrou_r = False

        while p is not None:
            if p == r:
                encontrou_r = True
                break
            p = p.prox

        if not encontrou_r:
            break

        if q == r:
            break

        q.valor, r.valor = r.valor, q.valor

        q = q.prox
        r = r.ant

    return lista