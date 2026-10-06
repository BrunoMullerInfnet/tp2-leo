import time

def mochila(itens, i, cap, contagem):
    contagem["chamadas"] += 1

    if i == len(itens) or cap == 0:
        return 0

    nome, peso, valor = itens[i]

    # se nao cabe, segue sem esse item
    if peso > cap:
        return mochila(itens, i + 1, cap, contagem)

    sem = mochila(itens, i + 1, cap, contagem)
    com = valor + mochila(itens, i + 1, cap - peso, contagem)

    if com > sem:
        return com
    return sem

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

    contagem = {"chamadas": 0}

    comeco = time.perf_counter()
    melhor = mochila(itens, 0, cap, contagem)
    gasto = time.perf_counter() - comeco

    print("\n===== SOLUCAO RECURSIVA =====")
    print(f"Valor maximo: {melhor}")
    print(f"Chamadas recursivas: {contagem['chamadas']}")
    print(f"Tempo de execucao: {gasto:.6f} segundos")

if __name__ == "__main__":
    main()
