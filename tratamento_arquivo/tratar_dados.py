import csv

# Nome do arquivo de entrada e saída
arquivo_txt = 'tratamento_arquivo/ler_pot.txt'
arquivo_csv = 'analise_dados/seeds/dados.csv'

# Dicionário para armazenar os dados
dados = {'id_registro': [], 'leitura_potenciometro': [], 'latitude': [], 'longitude': []}

# Função para limpar a string e converter para float se necessário
def limpar_valor(valor):
    return float(valor.strip()) if '.' in valor else valor.strip()

# Abrir o arquivo de texto e processar as linhas
with open(arquivo_txt, 'r') as arquivo:
    leitura_potenciometro = None

    for linha in arquivo:
        chave, valor = map(str.strip, linha.split(':', 1))

        if chave == 'Leitura Potenciometro':
            leitura_potenciometro = limpar_valor(valor)
            dados['leitura_potenciometro'].append(leitura_potenciometro)
        elif chave == 'Latitude':
            dados['latitude'].append(limpar_valor(valor))
        elif chave == 'Longitude':
            dados['longitude'].append(limpar_valor(valor))

# Determinar o número total de registros
num_registros = len(dados['leitura_potenciometro'])

# Escrever os dados no arquivo CSV
with open(arquivo_csv, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Escrever o cabeçalho
    writer.writerow(['id_registro', 'leitura_potenciometro', 'latitude', 'longitude'])
    
    # Escrever os dados
    for i in range(num_registros):
        writer.writerow([i + 1] + [dados[chave][i] for chave in ['leitura_potenciometro', 'latitude', 'longitude']])
