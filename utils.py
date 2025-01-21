import matplotlib.pyplot as plt
import pandas as pd
from metrics.qos import QoS

def plot_qos_metrics(users, metric_name, metric_values):
    """
    Plota um gráfico de barras para as métricas de QoS.
    """
    user_ids = [user.user_id for user in users]
    plt.bar(user_ids, metric_values, color='blue')
    plt.title(f"{metric_name} por Usuário")
    plt.xlabel("Usuários")
    plt.ylabel(metric_name)
    plt.show()

def export_qos_metrics(users, filename="qos_metrics.csv"):
    """
    Exporta métricas de QoS para um arquivo CSV.
    """
    data = {
        "User": [user.user_id for user in users],
        "Slice Type": [user.slice_type for user in users],
        "Latency (ms)": [
            QoS.calculate_latency(user.slice_type, penalty=getattr(user, "latency_penalty", 0))
            for user in users
        ],
        "Throughput (Mbps)": [QoS.calculate_throughput(user.slice_type) for user in users],
        "Jitter (ms)": [
            QoS.calculate_jitter(user.slice_type, penalty=getattr(user, "jitter_penalty", 0))
            for user in users
        ],
        "Packet Loss (%)": [QoS.calculate_packet_loss(user.slice_type) for user in users],
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Relatório salvo em {filename}")

def compare_qos_metrics(fixed_file, mobile_file):
    """
    Compara as métricas de QoS entre os cenários fixo e móvel.
    """
    fixed_data = pd.read_csv(fixed_file)
    mobile_data = pd.read_csv(mobile_file)

    metrics = ["Latency (ms)", "Throughput (Mbps)", "Jitter (ms)", "Packet Loss (%)"]
    for metric in metrics:
        plt.figure()
        plt.bar(fixed_data["User"], fixed_data[metric], color='blue', alpha=0.7, label='Fixo')
        plt.bar(mobile_data["User"], mobile_data[metric], color='orange', alpha=0.7, label='Mobilidade')
        plt.title(f"Comparação de {metric} entre Cenários")
        plt.xlabel("Usuários")
        plt.ylabel(metric)
        plt.legend()
        plt.show()


import pandas as pd
from metrics.qos import QoS
import matplotlib.pyplot as plt

def analyze_overload(users, filename="qos_overload_analysis.csv"):
    """
    Analisa o impacto da sobrecarga nas métricas de QoS.
    """
    data = {
        "User": [user.user_id for user in users],
        "Slice Type": [user.slice_type for user in users],
        "Latency with Penalty (ms)": [
            QoS.calculate_latency(user.slice_type, penalty=getattr(user, "latency_penalty", 0))
            for user in users
        ],
        "Jitter with Penalty (ms)": [
            QoS.calculate_jitter(user.slice_type, penalty=getattr(user, "jitter_penalty", 0))
            for user in users
        ],
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Análise de sobrecarga salva em {filename}")

def plot_overload(users):
    """
    Gera gráficos para visualizar o impacto da sobrecarga nas métricas.
    """
    user_ids = [user.user_id for user in users]
    latencies = [
        QoS.calculate_latency(user.slice_type, penalty=getattr(user, "latency_penalty", 0))
        for user in users
    ]
    jitters = [
        QoS.calculate_jitter(user.slice_type, penalty=getattr(user, "jitter_penalty", 0))
        for user in users
    ]

    # Plot Latência
    plt.bar(user_ids, latencies, color='red')
    plt.title("Latência com Sobrecarga")
    plt.xlabel("Usuários")
    plt.ylabel("Latência (ms)")
    plt.show()

    # Plot Jitter
    plt.bar(user_ids, jitters, color='purple')
    plt.title("Jitter com Sobrecarga")
    plt.xlabel("Usuários")
    plt.ylabel("Jitter (ms)")
    plt.show()
