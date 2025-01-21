class Cell:
    def __init__(self, cell_id, capacity):
        self.cell_id = cell_id
        self.capacity = capacity
        self.connected_users = []

    def connect_user(self, user):
        if len(self.connected_users) < self.capacity:
            self.connected_users.append(user)
            print(f"User {user.user_id} connected to Cell {self.cell_id}")
        else:
            # Penalidade incremental com base na sobrecarga
            overload = len(self.connected_users) - self.capacity + 1
            user.latency_penalty = 20 * overload  # Aumento de 20 ms por usuário extra
            user.jitter_penalty = 5 * overload  # Aumento de 5 ms por usuário extra
            print(f"Cell {self.cell_id} is overloaded! Applying penalties: "
                  f"Latency +{user.latency_penalty} ms, Jitter +{user.jitter_penalty} ms")

    def disconnect_user(self, user):
        if user in self.connected_users:
            self.connected_users.remove(user)
            print(f"User {user.user_id} disconnected from Cell {self.cell_id}")
