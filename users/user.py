# User
class User:
    def __init__(self, user_id, slice_type):
        """
        Inicializa um usuário com ID, tipo de slice, célula atual e controle de handovers.
        """
        self.user_id = user_id
        self.slice_type = slice_type  # Tipo de slice (eMBB, URLLC, mMTC)
        self.current_cell = None
        self.handover_count = 0  # Conta o número de handovers realizados
        self.last_handover_step = -1  # Time step do último handover

    def move_to_cell(self, new_cell, current_step):
        """
        Move o usuário para uma nova célula, registrando o handover.
        Respeita o intervalo mínimo entre handovers para reduzir o jitter.
        """
        if self.current_cell:
            self.current_cell.disconnect_user(self)

        new_cell.connect_user(self)
        self.current_cell = new_cell

        # Registra o handover
        self.handover_count += 1
        self.last_handover_step = current_step
        print(f"User {self.user_id} moved to Cell {new_cell.cell_id} (Handover #{self.handover_count})")

    def can_handover(self, current_step, min_interval=2):
        """
        Verifica se o usuário pode realizar um handover.
        O intervalo mínimo é configurável e pode ser maior para o slice URLLC.
        """
        if self.slice_type == "URLLC":
            min_interval += 1  # Aumenta o intervalo mínimo para URLLC

        return current_step - self.last_handover_step >= min_interval

