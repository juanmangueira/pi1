import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_distance_time(json_filename, graph_name):
    with open(json_filename, 'r') as file:
        data = json.load(file)

        distance = data["Distance"]
        time_difference = data["Time_Difference"]

        # Converter a string de tempo em um objeto timedelta
        time_diff = datetime.strptime(time_difference, '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')

        # Gerar os pontos de tempo com base na diferença de tempo fornecida
        num_points = 10
        time_interval = time_diff.total_seconds() / (num_points - 1)  # Ajuste para obter o tempo final correto
        time_points = [str(timedelta(seconds=i * time_interval)) for i in range(num_points)]

        # Gerar as distâncias correspondentes
        distances = [distance * (i / (num_points - 1)) for i in range(num_points)]

        plt.figure(figsize=(8, 6))
        plt.plot(time_points, distances, marker='o', linestyle='-')
        plt.title(f'Distance over Time - {graph_name}')
        plt.xlabel('Time')
        plt.ylabel('Distance')
        plt.grid(True)
        plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para melhor visualização
        plt.tight_layout()
        
        # Salvar o gráfico como uma imagem com o nome fornecido
        plt.savefig(f'{graph_name}.png')

# Chame a função com o nome do arquivo JSON e o nome do gráfico
plot_distance_time('dados.json', 'Graph_3')
