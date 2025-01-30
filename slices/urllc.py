#URLLC
class URLLC:
    def __init__(self, bandwidth, latency):
        self.bandwidth = bandwidth
        self.latency = latency

    def allocate_resources(self, user):
        print(f"Allocating URLLC resources to {user}. Bandwidth: {self.bandwidth} Mbps, Latency: {self.latency} ms")
