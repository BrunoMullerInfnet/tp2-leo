import asyncio
import os
import time

PASTA = "/dados/arquivos"

def contar(caminho):
    linhas = 0
    palavras = 0

    arq = open(caminho, "r", encoding="utf-8", errors="replace")

    for linha in arq:
        linhas += 1
        palavras += len(linha.split())

    arq.close()

    nome = os.path.basename(caminho)
    return nome, linhas, palavras

async def ler_um(caminho):
    # to_thread pra leitura nao segurar o event loop
    return await asyncio.to_thread(contar, caminho)

async def main():
    lista = []

    for nome in os.listdir(PASTA):
        caminho = os.path.join(PASTA, nome)
        if os.path.isfile(caminho):
            lista.append(caminho)

    lista.sort()

    if len(lista) == 0:
        print(f"Nenhum arquivo encontrado em {PASTA}")
        return

    comeco = time.perf_counter()

    tarefas = []
    for caminho in lista:
        tarefas.append(asyncio.create_task(ler_um(caminho)))

    resultados = await asyncio.gather(*tarefas)
    gasto = time.perf_counter() - comeco

    for nome, linhas, palavras in resultados:
        print(nome)
        print(f"Linhas: {linhas}")
        print(f"Palavras: {palavras}")
        print()

    print(f"Tempo total: {gasto:.2f} segundos")

if __name__ == "__main__":
    asyncio.run(main())
