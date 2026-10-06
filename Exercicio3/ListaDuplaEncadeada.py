import time

class No:
    def __init__(self, valor):
        self.ant = None
        self.valor = valor
        self.prox = None

class ListaDupla:
    def __init__(self):
        self.comeco = None
        self.ultimo = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.prox = self.comeco

        if self.comeco == None:
            self.ultimo = novo
        else:
            self.comeco.ant = novo

        self.comeco = novo

    def inserir_final(self, valor):
        novo = No(valor)
        novo.ant = self.ultimo

        if self.ultimo == None:
            self.comeco = novo
        else:
            self.ultimo.prox = novo

        self.ultimo = novo

    def buscar(self, valor):
        atual = self.comeco

        while atual != None:
            if atual.valor == valor:
                return atual
            atual = atual.prox

        return None

    def remover(self, valor):
        atual = self.buscar(valor)

        if atual == None:
            return False

        # acerta os dois lados antes de soltar o no
        if atual.ant == None:
            self.comeco = atual.prox
        else:
            atual.ant.prox = atual.prox

        if atual.prox == None:
            self.ultimo = atual.ant
        else:
            atual.prox.ant = atual.ant

        return True

    def listar_inicio_fim(self):
        partes = []
        atual = self.comeco

        while atual != None:
            partes.append(str(atual.valor))
            atual = atual.prox

        return " -> ".join(partes)

    def listar_fim_inicio(self):
        partes = []
        atual = self.ultimo

        while atual != None:
            partes.append(str(atual.valor))
            atual = atual.ant

        return " -> ".join(partes)

def tempo_busca(lista, valor):
    comeco = time.perf_counter()
    lista.buscar(valor)
    return time.perf_counter() - comeco

def main():
    lista = ListaDupla()

    for valor in [10, 20, 30, 40, 50]:
        lista.inserir_final(valor)

    lista.remover(30)

    print(lista.listar_inicio_fim())
    print(lista.listar_fim_inicio())

    grande = ListaDupla()

    for n in range(1, 100001):
        grande.inserir_final(n)

    t_ini = tempo_busca(grande, 10)
    t_meio = tempo_busca(grande, 50000)
    t_fim = tempo_busca(grande, 99990)

    print()
    print(f"Busca proxima ao inicio: {t_ini:.9f} segundos")
    print(f"Busca proxima ao meio: {t_meio:.9f} segundos")
    print(f"Busca proxima ao final: {t_fim:.9f} segundos")

if __name__ == "__main__":
    main()
