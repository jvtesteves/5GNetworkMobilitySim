class Cell:
    def __init__(self, cell_id, capacity):
        """
        Inicializa uma célula com ID, capacidade, lista de usuários conectados, estado e nível de interferência.
        """
        self.cell_id = cell_id
        self.capacity = capacity
        self.connected_users = []
        self.is_active = True  # Indica se a célula está ativa
        self.failure_timer = 0  # Temporizador para falha temporária
        self.interference_level = 0  # Nível de interferência causado pelas células vizinhas
        self.signal_strength = 100  # Intensidade do sinal da célula (0-100)

    def connect_user(self, user):
        """
        Conecta um usuário à célula se ela estiver ativa e não estiver sobrecarregada.
        """
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
        """
        Desconecta o usuário da célula.
        """
        if user in self.connected_users:
            self.connected_users.remove(user)
            print(f"User {user.user_id} disconnected from Cell {self.cell_id}")

    def activate(self):
        """
        Ativa a célula.
        """
        self.is_active = True
        print(f"Cell {self.cell_id} is now active.")

    def deactivate(self, duration):
        """
        Desativa a célula por um determinado número de time steps.
        """
        self.is_active = False
        self.failure_timer = duration
        print(f"Cell {self.cell_id} has been deactivated for {duration} time steps.")

    def update_status(self):
        """
        Atualiza o status da célula, reativando-a quando o timer chega a zero.
        """
        if not self.is_active and self.failure_timer > 0:
            self.failure_timer -= 1
            if self.failure_timer == 0:
                self.activate()

    def calculate_interference(self, adjacent_cells):
        """
        Calcula o nível de interferência baseado no número de usuários nas células vizinhas.
        Quanto mais usuários, maior a interferência.
        """
        self.interference_level = sum(len(cell.connected_users) for cell in adjacent_cells if cell.is_active)
        self.signal_strength = max(100 - (self.interference_level * 5), 20)  # Reduz a intensidade do sinal conforme a interferência
        print(f"Cell {self.cell_id} has interference level: {self.interference_level}, Signal strength: {self.signal_strength}")

    def get_signal_strength(self):
        """
        Retorna a intensidade atual do sinal da célula.
        """
        return self.signal_strength

