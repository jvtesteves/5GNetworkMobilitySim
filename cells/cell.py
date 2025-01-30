class Cell:
    def __init__(self, cell_id, capacity):
        self.cell_id = cell_id
        self.capacity = capacity
        self.connected_users = []
        self.is_active = True  # Indica se a célula está ativa
        self.failure_timer = 0  # Temporizador para falha temporária

    def connect_user(self, user):
        if not self.is_active:
            print(f"Cell {self.cell_id} is currently inactive. User {user.user_id} cannot connect.")
            return

        if len(self.connected_users) < self.capacity:
            self.connected_users.append(user)
            print(f"User {user.user_id} connected to Cell {self.cell_id}")
        else:
            overload = len(self.connected_users) - self.capacity + 1
            user.latency_penalty = 20 * overload
            user.jitter_penalty = 5 * overload
            print(f"Cell {self.cell_id} is overloaded! Applying penalties: "
                  f"Latency +{user.latency_penalty} ms, Jitter +{user.jitter_penalty} ms")

    def disconnect_user(self, user):
        if user in self.connected_users:
            self.connected_users.remove(user)
            print(f"User {user.user_id} disconnected from Cell {self.cell_id}")

    def activate(self):
        self.is_active = True
        print(f"Cell {self.cell_id} is now active.")

    def deactivate(self, duration):
        self.is_active = False
        self.failure_timer = duration
        print(f"Cell {self.cell_id} has been deactivated for {duration} time steps.")

    def update_status(self):
        if not self.is_active:
            if self.failure_timer > 0:
                self.failure_timer -= 1
            if self.failure_timer == 0:
                self.activate()
