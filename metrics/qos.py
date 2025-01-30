import random

class QoS:
    @staticmethod
    def calculate_latency(slice_type, penalty=0):
        base_latency = random.uniform(1, 50) if slice_type == "eMBB" else random.uniform(0.1, 10)
        return base_latency + penalty
    #throughput
    @staticmethod
    def calculate_throughput(slice_type):
        if slice_type == "eMBB":
            return random.uniform(50, 100)
        elif slice_type == "URLLC":
            return random.uniform(10, 50)
        else:
            return random.uniform(1, 10)
    #jitter
    @staticmethod
    def calculate_jitter(slice_type, penalty=0):
        base_jitter = random.uniform(0.01, 5) if slice_type == "URLLC" else random.uniform(5, 20)
        return base_jitter + penalty
    #packet_loss
    @staticmethod
    def calculate_packet_loss(slice_type):
        if slice_type == "mMTC":
            return random.uniform(0, 1)
        else:
            return random.uniform(0, 0.1)
