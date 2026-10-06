def achar(lab, simbolo):
    for lin in range(len(lab)):
        for col in range(len(lab[lin])):
            if lab[lin][col] == simbolo:
                return lin, col

    return None

def andar(lab, lin, col, vistos):
    if lab[lin][col] == "E":
        return True

    vistos.add((lin, col))

    # cima, baixo, esquerda, direita
    passos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dl, dc in passos:
        nl = lin + dl
        nc = col + dc

        if nl < 0 or nl >= len(lab):
            continue
        if nc < 0 or nc >= len(lab[nl]):
            continue
        if lab[nl][nc] == "#":
            continue
        if (nl, nc) in vistos:
            continue

        if andar(lab, nl, nc, vistos):
            if lab[lin][col] == " ":
                lab[lin][col] = "."
            return True

    return False

def main():
    arq = open("/dados/labirinto.txt", "r", encoding="utf-8")
    lab = []

    for linha in arq:
        lab.append(list(linha.rstrip("\n")))

    arq.close()

    inicio = achar(lab, "S")
    saida = achar(lab, "E")

    if inicio == None or saida == None:
        print("Inicio ou saida nao encontrados.")
        return

    achou = andar(lab, inicio[0], inicio[1], set())

    print("\n===== LABIRINTO =====")

    for linha in lab:
        print("".join(linha))

    if achou:
        print("\nCaminho encontrado!")
    else:
        print("\nNenhum caminho encontrado!")

if __name__ == "__main__":
    main()
