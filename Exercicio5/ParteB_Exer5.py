import time

def mochila_pd(itens, cap):
    qtd = len(itens)
    tab = []
    estados = 0

    for i in range(qtd + 1):
        linha = [0] * (cap + 1)
        tab.append(linha)

    for i in range(1, qtd + 1):
        nome, peso, valor = itens[i - 1]

        for c in range(cap + 1):
            # cada casa da tabela conta como um estado
            estados += 1

            if peso > c:
                tab[i][c] = tab[i - 1][c]
            else:
                sem = tab[i - 1][c]
                com = valor + tab[i - 1][c - peso]

                if com > sem:
                    tab[i][c] = com
                else:
                    tab[i][c] = sem

    return tab[qtd][cap], estados

def main():
    arq = open("/dados/mochila.txt", "r", encoding="utf-8")

    qtd, cap = arq.readline().split()
    qtd = int(qtd)
    cap = int(cap)

    itens = []
    for n in range(qtd):
        nome, peso, valor = arq.readline().split()
        itens.append((nome, int(peso), int(valor)))

    arq.close()

    comeco = time.perf_counter()
    melhor, estados = mochila_pd(itens, cap)
    gasto = time.perf_counter() - comeco

    print("\n===== PROGRAMACAO DINAMICA =====")
    print(f"Valor maximo: {melhor}")
    print(f"Estados calculados: {estados}")
    print(f"Tempo de execucao: {gasto:.6f} segundos")

if __name__ == "__main__":
    main()
