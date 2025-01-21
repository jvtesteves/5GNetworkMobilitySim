from cells.cell import Cell
from users.user import User
from mobility import simulate_mobility
from metrics.qos import QoS
from utils import plot_qos_metrics, export_qos_metrics, compare_qos_metrics, analyze_overload, plot_overload

def simulate_fixed(users, cells):
    """
    Simula os usuários fixos em uma célula específica (célula 0 neste caso).
    """
    for user in users:
        user.move_to_cell(cells[0])  # Todos os usuários conectados à célula 0

def main():
    # Criar células
    cells = [Cell(cell_id=i, capacity=5) for i in range(5)]

    # Criar usuários
    users = [
        User(user_id=i + 1, slice_type="eMBB") if i % 3 == 0 else
        User(user_id=i + 1, slice_type="URLLC") if i % 3 == 1 else
        User(user_id=i + 1, slice_type="mMTC")
        for i in range(10)  # 10 usuários
    ]

    # Mapa de adjacência para mobilidade baseada em proximidade
    adjacency_map = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }

    # Simulação Fixa
    print("Simulação Fixa:")
    simulate_fixed(users, cells)

    # Coletar métricas para simulação fixa
    print("\nMétricas de QoS na Simulação Fixa:")
    export_qos_metrics(users, filename="qos_metrics_fixa.csv")

    # Simulação com Mobilidade
    print("\nSimulação com Mobilidade:")
    simulate_mobility(users, cells, adjacency_map, time_steps=10)

    # Coletar métricas para simulação com mobilidade
    print("\nMétricas de QoS na Simulação com Mobilidade:")
    export_qos_metrics(users, filename="qos_metrics_mobilidade.csv")

    # Comparar métricas
    compare_qos_metrics("qos_metrics_fixa.csv", "qos_metrics_mobilidade.csv")

    # Analisar sobrecarga
    analyze_overload(users, filename="qos_overload_analysis.csv")

    # Plotar impacto da sobrecarga
    plot_overload(users)

if __name__ == "__main__":
    main()
