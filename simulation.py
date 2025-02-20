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
        user.move_to_cell(cells[0], current_step=0)  # Todos os usuários conectados à célula 0

def trigger_cell_failures(cells, probability=0.2, duration=3):
    """
    Deativa aleatoriamente células com uma determinada probabilidade.
    Durante a desativação, a célula não aceitará novos usuários, e os conectados serão forçados a se mover.
    """
    for cell in cells:
        if random.random() < probability and cell.is_active:
            cell.deactivate(duration)

def calculate_interference_for_all_cells(cells, adjacency_map):
    """
    Calcula a interferência para todas as células com base no número de usuários nas células vizinhas.
    """
    for cell in cells:
        adjacent_cell_ids = adjacency_map.get(cell.cell_id, [])
        adjacent_cells = [adj_cell for adj_cell in cells if adj_cell.cell_id in adjacent_cell_ids]
        cell.calculate_interference(adjacent_cells)

def main():
    # Criar células com capacidade limitada e estado inicial ativo
    cells = [Cell(cell_id=i, capacity=5) for i in range(5)]

    # Criar usuários associados a diferentes slices de rede
    users = [
        User(user_id=i + 1, slice_type="eMBB") if i % 3 == 0 else
        User(user_id=i + 1, slice_type="URLLC") if i % 3 == 1 else
        User(user_id=i + 1, slice_type="mMTC")
        for i in range(10)
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

    # Simulação do cenário com mobilidade, falhas temporárias, interferência e handover otimizado
    print("\nSimulação com Mobilidade, Falhas Temporárias, Interferência e Handover Otimizado:")
    for t in range(10):
        trigger_cell_failures(cells)
        calculate_interference_for_all_cells(cells, adjacency_map)
        simulate_mobility(users, cells, adjacency_map, time_steps=1, current_step=t)

    # Coletar e exportar métricas do cenário com mobilidade
    print("\nMétricas de QoS na Simulação com Mobilidade, Falhas Temporárias, Interferência e Handover Otimizado:")
    export_qos_metrics(users, filename="qos_metrics_mobilidade_handover.csv")

    # Comparar as métricas entre os dois cenários
    compare_qos_metrics("qos_metrics_fixa.csv", "qos_metrics_mobilidade_handover.csv")

    # Analisar o impacto da sobrecarga e exportar os resultados
    analyze_overload(users, filename="qos_overload_analysis.csv")

    # Gerar gráficos do impacto da sobrecarga
    plot_overload(users)

if __name__ == "__main__":
    main()

