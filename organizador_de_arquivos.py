import os

# Pegar nome do arquivo
# Pegar a extensao do arquivo
# Criar pastas
# Mover os arquivos para as pastas correspondentes

audios_ext = ['.mp3', '.wav']
imagens_ext = ['.jpg', '.jpeg', '.png']
docs_ext = ['.txt', '.log', '.pdf']
videos_ext = ['.mp4', '.mov', '.pdf']

def organizar(diretorio):
    AUDIOS_DIR = os.path.join(diretorio, 'audios') # Guarda caminho para a pasta
    IMAGENS_DIR = os.path.join(diretorio, 'imagens')
    DOCS_DIR = os.path.join(diretorio, 'docs')
    VIDEOS_DIR = os.path.join(diretorio, 'videos')
    OUTROS_DIR = os.path.join(diretorio, 'outros')

    if not os.path.isdir(AUDIOS_DIR): # Verifica se a pasta nao existe
        os.mkdir(AUDIOS_DIR) # Se a pasta nao existir, uma pasta com o respectivo caminho sera criada

    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)

    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)

    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)

    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)

    nomes_arquivos = os.listdir(diretorio) # Guarda os nomes dos arquivos em uma lista
    nova_pasta = ''

    for arquivo in nomes_arquivos:
        extensao = str.lower(pegar_extensao(arquivo)) # Pega a extensao do arquivo e joga pra lower case

        if os.path.isfile(os.path.join(diretorio, arquivo)): # Verifica se o arquivo existe

            if extensao in audios_ext: # Verifica a qual tipo o arquivo pertence
                nova_pasta = AUDIOS_DIR # Guarda o arquivo para move-lo para outra pasta

            elif extensao in imagens_ext:
                nova_pasta  = IMAGENS_DIR
            
            elif extensao in docs_ext:
                nova_pasta = DOCS_DIR

            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR

            else:
                nova_pasta = OUTROS_DIR

            velho = os.path.join(diretorio, arquivo) # Caminho antigo do arquivo
            novo = os.path.join(nova_pasta, arquivo) # caminho novo do arquivo

            os.rename(velho, novo) # Move o arquivo

            print(f'Moveu {velho} --> {novo}')


def pegar_extensao(nome):
    index = nome.rfind('.') # Procura a extensao do arquivo e guarda na variavel index
    
    return nome[index:]


if __name__ == '__main__':
    # Troque pelo nome do diretório desejado
    organizar('teste_organizador_de_arquivos')
