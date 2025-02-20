import random

def simulate_mobility(users, cells, adjacency_map, time_steps, current_step):
    """
    Simula a mobilidade dos usuários entre células, considerando falhas, interferência das células vizinhas e sinal da célula.
    O usuário troca de célula apenas se a nova célula tiver um sinal significativamente melhor.
    """
    for t in range(time_steps):
        print(f"Time Step {t}")

        # Atualizar o status das células (reativar após falha)
        for cell in cells:
            cell.update_status()

        # Calcular interferência para cada célula
        for cell in cells:
            adjacent_cell_ids = adjacency_map.get(cell.cell_id, [])
            adjacent_cells = [adj_cell for adj_cell in cells if adj_cell.cell_id in adjacent_cell_ids]
            cell.calculate_interference(adjacent_cells)

        # Movimentação dos usuários com critério de sinal
        for user in users:
            if user.current_cell:
                # Se a célula do usuário estiver desativada, forçar o movimento
                if not user.current_cell.is_active:
                    print(f"User {user.user_id} is moving because Cell {user.current_cell.cell_id} is inactive.")
                    adjacent_cell_ids = adjacency_map.get(user.current_cell.cell_id, [])
                    adjacent_cells = [cell for cell in cells if cell.cell_id in adjacent_cell_ids and cell.is_active]

                    if adjacent_cells:
                        new_cell = max(adjacent_cells, key=lambda c: c.get_signal_strength())
                        user.move_to_cell(new_cell, current_step)
                    else:
                        print(f"No active adjacent cells for User {user.user_id}.")
                else:
                    # Verificar se o usuário pode fazer handover baseado no sinal
                    adjacent_cell_ids = adjacency_map.get(user.current_cell.cell_id, [])
                    adjacent_cells = [cell for cell in cells if cell.cell_id in adjacent_cell_ids and cell.is_active]

                    if adjacent_cells:
                        best_cell = max(adjacent_cells, key=lambda c: c.get_signal_strength())
                        if best_cell.get_signal_strength() > user.current_cell.get_signal_strength() + 10 and user.can_handover(current_step):
                            user.move_to_cell(best_cell, current_step)
                            print(f"User {user.user_id} performed handover to Cell {best_cell.cell_id} due to better signal strength")

