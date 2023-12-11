import csv
import os

# Função para limpar a string e converter para float se necessário
def limpar_valor(valor):
    return float(valor.strip()) if '.' in valor else valor.strip()

# Função para processar o arquivo de texto e gerar o arquivo CSV
def processar_arquivo(arquivo_txt, arquivo_csv, objetivo):
    # Dicionário para armazenar os dados
    dados = {'id_lancamento': [], 'latitude': [], 'longitude': [], 'objetivo': []}

    # Verificar se o arquivo CSV já existe
    existe_arquivo = os.path.exists(arquivo_csv)

    # Abrir o arquivo de texto e processar as linhas
    with open(arquivo_txt, 'r') as arquivo:

        for linha in arquivo:
            chave, valor = map(str.strip, linha.split(':', 1))

            if chave == 'Latitude':
                dados['latitude'].append(limpar_valor(valor))
            elif chave == 'Longitude':
                dados['longitude'].append(limpar_valor(valor))

    # Determinar o número total de registros
    num_registros = len(dados['latitude'])

    # Adicionar a variável objetivo aos dados
    dados['objetivo'] = [objetivo] * num_registros

    # Adicionar o cabeçalho se o arquivo não existir
    with open(arquivo_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if not existe_arquivo:
            writer.writerow(['id_lancamento', 'latitude', 'longitude', 'objetivo'])

        # Escrever os dados adicionando a nova coluna
        for i in range(num_registros):
            writer.writerow([i + 1] + [dados[chave][i] for chave in ['latitude', 'longitude', 'objetivo']])

# Nome do arquivo de entrada e saída
arquivo_txt = '/home/juanmangueira/pi1/tratamento_arquivo/ler_pot.txt'
pasta_saida = '/home/juanmangueira/pi1/analise_dados/seeds'
arquivo_csv = os.path.join(pasta_saida, 'dados.csv')

# Cria a pasta de saída se não existir
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Solicitar a variável objetivo
objetivo = input('Digite a variável objetivo: ')

# Verificar se a entrada é um número
try:
    objetivo = float(objetivo)
except ValueError:
    print('Por favor, insira um valor numérico para a variável objetivo.')
    exit()

# Processar o arquivo e adicionar a nova coluna
processar_arquivo(arquivo_txt, arquivo_csv, objetivo)

print(f'O arquivo CSV foi atualizado com a nova coluna e salvo em: {arquivo_csv}')
