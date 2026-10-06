#include <ctype.h>
#include <dirent.h>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

#define _POSIX_C_SOURCE 200809L
#define PASTA "/dados/arquivos"
#define LIMITE 1000

typedef struct {
    char nome[256];
    long linhas;
    long palavras;
} Contagem;

int conta_palavras(const char *texto) {
    int total = 0;
    int dentro = 0;

    while (*texto != '\0') {
        if (isspace((unsigned char) *texto)) {
            dentro = 0;
        } else if (dentro == 0) {
            total++;
            dentro = 1;
        }

        texto++;
    }

    return total;
}

void ler_arquivo(Contagem *item) {
    char caminho[512];
    char *linha = NULL;
    size_t tam = 0;
    FILE *arq;

    snprintf(caminho, sizeof(caminho), "%s/%s", PASTA, item->nome);

    arq = fopen(caminho, "r");
    if (arq == NULL) {
        printf("Erro ao abrir: %s\n", item->nome);
        return;
    }

    while (getline(&linha, &tam, arq) != -1) {
        item->linhas++;
        item->palavras += conta_palavras(linha);
    }

    free(linha);
    fclose(arq);
}

int main(void) {
    DIR *dir;
    struct dirent *ent;
    Contagem lista[LIMITE] = {0};
    int qtd = 0;
    int i;
    double comeco;
    double gasto;

    dir = opendir(PASTA);
    if (dir == NULL) {
        printf("Nao foi possivel abrir %s\n", PASTA);
        return 1;
    }

    while (qtd < LIMITE && (ent = readdir(dir)) != NULL) {
        /* pula . .. e o que comeca com ponto */
        if (ent->d_name[0] == '.') {
            continue;
        }

        snprintf(lista[qtd].nome, 256, "%s", ent->d_name);
        qtd++;
    }

    closedir(dir);

    comeco = omp_get_wtime();

    /* cada iteracao pode rodar em uma thread */
    #pragma omp parallel for
    for (i = 0; i < qtd; i++) {
        ler_arquivo(&lista[i]);
    }

    gasto = omp_get_wtime() - comeco;

    for (i = 0; i < qtd; i++) {
        printf("%s\n", lista[i].nome);
        printf("Linhas: %ld\n", lista[i].linhas);
        printf("Palavras: %ld\n\n", lista[i].palavras);
    }

    printf("Tempo total: %.6f segundos\n", gasto);
    return 0;
}
