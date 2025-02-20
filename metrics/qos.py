import random

class QoS:
    @staticmethod
    def calculate_latency(slice_type, penalty=0, interference=0):
        """
        Calcula a latência considerando o tipo de slice, penalidades e interferência.
        """
        base_latency = random.uniform(1, 50) if slice_type == "eMBB" else random.uniform(0.1, 10)
        return base_latency + penalty + (0.5 * interference)  # Interferência adiciona 0.5 ms por unidade

    @staticmethod
    def calculate_throughput(slice_type, interference=0):
        """
        Calcula o throughput considerando o tipo de slice e a interferência.
        """
        if slice_type == "eMBB":
            base_throughput = random.uniform(50, 100)
        elif slice_type == "URLLC":
            base_throughput = random.uniform(10, 50)
        else:
            base_throughput = random.uniform(1, 10)

        # Reduz o throughput em 2% por unidade de interferência, garantindo um mínimo de 1 Mbps
        throughput = base_throughput * (1 - 0.02 * interference)
        return max(throughput, 1)

    @staticmethod
    def calculate_jitter(slice_type, penalty=0, interference=0):
        """
        Calcula o jitter considerando o tipo de slice, penalidades e interferência.
        """
        base_jitter = random.uniform(0.01, 5) if slice_type == "URLLC" else random.uniform(5, 20)
        return base_jitter + penalty + (0.3 * interference)  # Interferência adiciona 0.3 ms por unidade

    @staticmethod
    def calculate_packet_loss(slice_type, interference=0):
        """
        Calcula a perda de pacotes considerando o tipo de slice e a interferência.
        """
        base_loss = random.uniform(0, 1) if slice_type == "mMTC" else random.uniform(0, 0.1)
        # A interferência aumenta a perda de pacotes em 0.05% por unidade, até um máximo de 5%
        return min(base_loss + (0.0005 * interference), 0.05)

