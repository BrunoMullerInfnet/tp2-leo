import time

def trocar(vetor, a, b):
    aux = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = aux

def particionar(vetor, esq, dir):
    meio = (esq + dir) // 2
    trocar(vetor, meio, dir)

    pivo = vetor[dir]
    i = esq - 1

    for j in range(esq, dir):
        if vetor[j] <= pivo:
            i += 1
            trocar(vetor, i, j)

    trocar(vetor, i + 1, dir)
    return i + 1

def quickselect(vetor, esq, dir, alvo):
    # vai so pro lado onde o 1000o menor pode estar
    while esq <= dir:
        pos = particionar(vetor, esq, dir)

        if pos == alvo:
            return vetor[pos]

        if alvo < pos:
            dir = pos - 1
        else:
            esq = pos + 1

    raise ValueError("Posicao invalida")

def main():
    arq = open("/dados/numeros.txt", "r", encoding="utf-8")
    texto = arq.read()
    arq.close()

    numeros = []
    for pedaco in texto.split():
        numeros.append(int(pedaco))

    comeco = time.perf_counter()
    milesimo = quickselect(numeros, 0, len(numeros) - 1, 999)
    gasto = time.perf_counter() - comeco

    print(f"1000o menor numero: {milesimo}")
    print(f"Tempo de execucao: {gasto:.6f} segundos")

if __name__ == "__main__":
    main()
