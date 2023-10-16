#include <stdio.h>
#include <windows.h>

int main() {
    WIN32_FIND_DATAW FindFileData;
    HANDLE hFindFile;
    LPCWSTR folderPath = L"C:\\Users\\lucio\\OneDrive\\Área de Trabalho\\Estudos\\pomodoro\\songs\\musics\\";
    LPCWSTR filePattern = L"*.*";

    // Abra um arquivo para escrever os nomes dos arquivos
    FILE *outputFile = fopen("nomes_arquivos.txt", "w");

    if (outputFile == NULL) {
        wprintf(L"Erro ao abrir o arquivo de saída.\n");
        return 1;
    }

    // Construa o caminho completo do diretório
    WCHAR filePath[MAX_PATH];
    wcscpy(filePath, folderPath);
    wcscat(filePath, filePattern);

    hFindFile = FindFirstFileW(filePath, &FindFileData);

    if (hFindFile == INVALID_HANDLE_VALUE) {
        wprintf(L"Nenhum arquivo encontrado na pasta.\n");
    } else {
        do {
            // Escreva o nome do arquivo no arquivo de saída
            fwprintf(outputFile, L"%s\n", FindFileData.cFileName);
        } while (FindNextFileW(hFindFile, &FindFileData) != 0);

        FindClose(hFindFile);
        fclose(outputFile);
        wprintf(L"Lista de nomes de arquivos gravada em 'nomes_arquivos.txt'.\n");
    }

    return 0;
}
