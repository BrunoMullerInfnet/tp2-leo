import time

def trocar(vetor, a, b):
    aux = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = aux

def particionar(vetor, esq, dir, contagem):
    # joga o do meio pro fim pra nao pegar sempre a ponta
    meio = (esq + dir) // 2
    trocar(vetor, meio, dir)

    pivo = vetor[dir]
    i = esq - 1

    for j in range(esq, dir):
        contagem["comparacoes"] += 1

        if vetor[j] <= pivo:
            i += 1
            trocar(vetor, i, j)

    trocar(vetor, i + 1, dir)
    return i + 1

def quicksort(vetor, esq, dir, contagem):
    if esq >= dir:
        return

    pos = particionar(vetor, esq, dir, contagem)

    # conta as duas chamadas daqui, a primeira do main fica de fora
    contagem["chamadas"] += 2

    quicksort(vetor, esq, pos - 1, contagem)
    quicksort(vetor, pos + 1, dir, contagem)

def main():
    arq = open("/dados/numeros.txt", "r", encoding="utf-8")
    texto = arq.read()
    arq.close()

    numeros = []
    for pedaco in texto.split():
        numeros.append(int(pedaco))

    contagem = {"comparacoes": 0, "chamadas": 0}

    comeco = time.perf_counter()
    quicksort(numeros, 0, len(numeros) - 1, contagem)
    milesimo = numeros[999]
    gasto = time.perf_counter() - comeco

    print(f"1000o menor numero: {milesimo}")
    print(f"Comparacoes: {contagem['comparacoes']}")
    print(f"Chamadas recursivas: {contagem['chamadas']}")
    print(f"Tempo de execucao: {gasto:.6f} segundos")

if __name__ == "__main__":
    main()
