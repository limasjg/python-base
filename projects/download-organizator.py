import os
import shutil

# Variáveis Globais (Configurações)
CAMINHO_DOWNLOADS = os.path.expanduser("~/Downloads")
MAPEAMENTO = {
    ".pdf": os.path.expanduser("~/Documentos/pdfs"),
    ".xlsx": os.path.expanduser("~/Documentos/Excel"),
    ".jpeg": os.path.expanduser("~/Imagens"),
    ".mp3": os.path.expanduser("~/Music")
}

def listar_arquivos(diretorio):
    """Retorna uma lista de tuplas (nome_completo, extensao)"""
    arquivos_encontrados = []
    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        if os.path.isfile(caminho_completo):
            _, extensao = os.path.splitext(item)
            arquivos_encontrados.append((item, extensao.lower()))
    return arquivos_encontrados

def mover_arquivo(diretorio_origem, nome_arquivo, pasta_destino):
    """Lógica específica para mover um único arquivo"""
    origem = os.path.join(diretorio_origem, nome_arquivo)
    destino_pasta = os.path.join(diretorio_origem, pasta_destino)
    
    if not os.path.exists(destino_pasta):
        os.makedirs(destino_pasta)
    
    shutil.move(origem, os.path.join(destino_pasta, nome_arquivo))
    print(f"Sucesso: {nome_arquivo} -> {pasta_destino}")

def main():
    print("Iniciando organização...")
    arquivos = listar_arquivos(CAMINHO_DOWNLOADS)
    
    for nome, ext in arquivos:
        if ext in MAPEAMENTO:
            mover_arquivo(CAMINHO_DOWNLOADS, nome, MAPEAMENTO[ext])

if __name__ == "__main__":
    main()