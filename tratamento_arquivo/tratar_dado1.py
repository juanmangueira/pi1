import sys
import json
import csv
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime

def echo(phrase: str) -> None:
    print(phrase)

def read_txt(filename: str) -> list:
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def save_data(filename: str, data: dict) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convertendo graus para radianos
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Raio da Terra em km
    R = 6371.0

    # Diferença das latitudes e longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distância em km
    distance = R * c * 1000
    return distance

def calculate_time_difference(time1, time2):
    # Calculando a diferença de tempo
    time_format = '%H:%M:%S'
    time_obj1 = datetime.strptime(time1, time_format)
    time_obj2 = datetime.strptime(time2, time_format)
    time_difference = time_obj2 - time_obj1
    return str(time_difference)

def json_to_csv(json_filename, csv_filename):
    # Abrindo o arquivo JSON e o arquivo CSV
    with open(json_filename, 'r') as json_file, open(csv_filename, 'w', newline='') as csv_file:
        data = json.load(json_file)

        # Obtendo os cabeçalhos a partir das chaves do dicionário
        headers = list(data.keys())

        # Criando o escritor CSV
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        # Escrevendo o cabeçalho no arquivo CSV
        writer.writeheader()

        # Escrevendo os dados no arquivo CSV
        writer.writerow(data)



def main() -> int:
    # Lendo os dados do arquivo de texto
    txt_data = read_txt('tratamento_arquivo/ler_pot.txt')

    # Encontrando as coordenadas iniciais (primeira ocorrência de Latitude e Longitude)
    initial_lat, initial_lon = None, None
    for line in txt_data:
        if line.startswith('Latitude'):
            initial_lat = float(line.split(': ')[1])
        elif line.startswith('Longitude'):
            initial_lon = float(line.split(': ')[1])
        if initial_lat is not None and initial_lon is not None:
            break

    # Encontrando as coordenadas finais (última ocorrência de Latitude e Longitude)
    final_lat, final_lon = None, None
    for line in reversed(txt_data):
        if line.startswith('Latitude'):
            final_lat = float(line.split(': ')[1])
        elif line.startswith('Longitude'):
            final_lon = float(line.split(': ')[1])
        if final_lat is not None and final_lon is not None:
            break

    # Encontrando os horários inicial e final
    initial_time, final_time = None, None
    for line in txt_data:
        if line.startswith('Hora'):
            if initial_time is None:
                initial_time = line.split(': ')[1]
            final_time = line.split(': ')[1]

    # Calculando a distância entre as coordenadas
    distance = calculate_distance(initial_lat, initial_lon, final_lat, final_lon)

    # Calculando a diferença de tempo
    time_difference = calculate_time_difference(initial_time, final_time)

    tempo_segundos = datetime.strptime(final_time, '%H:%M:%S') - datetime.strptime(initial_time, '%H:%M:%S')
    tempo_segundos = tempo_segundos.total_seconds()
    velocidade_media = distance / tempo_segundos if tempo_segundos != 0 else 0

    # Calculando a aceleração média (supondo que haja um tempo decorrido)
    # Supondo uma variação de velocidade, aqui usaremos a velocidade média como exemplo
    variacao_velocidade = velocidade_media
    aceleracao_media = variacao_velocidade / tempo_segundos if tempo_segundos != 0 else 0


    # Criando um dicionário com os dados a serem salvos no JSON
    data_to_save = {
        "Distance": distance,
        "Time_Difference": time_difference,  # Adicionando a diferença de tempo
        "Speed":velocidade_media,
        "Aceleracao":aceleracao_media,
    }

    # Salvando os dados em um arquivo JSON
    save_data('dados1.json', data_to_save)

    json_to_csv('dados.json', 'dados.csv')


    return 0

if __name__ == '__main__':
    sys.exit(main())
