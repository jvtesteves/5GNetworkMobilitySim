from cells.cell import Cell
from users.user import User
from mobility import simulate_mobility
from metrics.qos import QoS
from utils import plot_qos_metrics, export_qos_metrics, compare_qos_metrics, analyze_overload, plot_overload
import random  # Importado para lidar com a escolha aleatória de falhas nas células

def simulate_fixed(users, cells):
    """
    Simula os usuários fixos em uma célula específica (célula 0 neste caso).
    Todos os usuários são conectados à mesma célula e permanecem nela durante a simulação fixa.
    """
    for user in users:
        user.move_to_cell(cells[0])  # Todos os usuários conectados à célula 0

def trigger_cell_failures(cells, probability=0.2, duration=3):
    """
    Deativa aleatoriamente células com uma determinada probabilidade.
    Durante a desativação, a célula não aceitará novos usuários, e os conectados serão forçados a se mover.
    :param cells: Lista de células da rede.
    :param probability: Probabilidade de uma célula ser desativada.
    :param duration: Duração da falha temporária.
    """
    for cell in cells:
        if random.random() < probability and cell.is_active:  # Verifica se a célula deve ser desativada
            cell.deactivate(duration)  # Desativa a célula por um número de time steps especificado

def main():
    # Criar células com capacidade limitada e estado inicial ativo
    cells = [Cell(cell_id=i, capacity=5) for i in range(5)]

    # Criar usuários associados a diferentes slices de rede
    users = [
        User(user_id=i + 1, slice_type="eMBB") if i % 3 == 0 else
        User(user_id=i + 1, slice_type="URLLC") if i % 3 == 1 else
        User(user_id=i + 1, slice_type="mMTC")
        for i in range(10)  # 10 usuários no total
    ]

    # Mapa de adjacência para mobilidade baseada em proximidade
    adjacency_map = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }

    # Simulação do cenário fixo (sem mobilidade)
    print("Simulação Fixa:")
    simulate_fixed(users, cells)

    # Coletar e exportar métricas do cenário fixo
    print("\nMétricas de QoS na Simulação Fixa:")
    export_qos_metrics(users, filename="qos_metrics_fixa.csv")

    # Simulação do cenário com mobilidade e falhas temporárias nas células
    print("\nSimulação com Mobilidade e Falhas Temporárias:")
    for t in range(10):  # Simula 10 time steps com mobilidade
        trigger_cell_failures(cells)  # Deativa aleatoriamente células a cada time step
        simulate_mobility(users, cells, adjacency_map, time_steps=1)  # Executa a mobilidade por 1 time step

    # Coletar e exportar métricas do cenário com mobilidade e falhas
    print("\nMétricas de QoS na Simulação com Mobilidade e Falhas Temporárias:")
    export_qos_metrics(users, filename="qos_metrics_mobilidade_falhas.csv")

    # Comparar as métricas entre os dois cenários
    compare_qos_metrics("qos_metrics_fixa.csv", "qos_metrics_mobilidade_falhas.csv")

    # Analisar o impacto da sobrecarga e exportar os resultados
    analyze_overload(users, filename="qos_overload_analysis.csv")

    # Gerar gráficos do impacto da sobrecarga
    plot_overload(users)

if __name__ == "__main__":
    main()

