import random

def simulate_mobility(users, cells, adjacency_map, time_steps):
    """
    Simula a mobilidade dos usuários entre células, considerando falhas e interferência das células vizinhas.
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

        # Movimentação dos usuários
        for user in users:
            if user.current_cell:
                # Se a célula do usuário estiver desativada, forçar o movimento
                if not user.current_cell.is_active:
                    print(f"User {user.user_id} is moving because Cell {user.current_cell.cell_id} is inactive.")
                    adjacent_cell_ids = adjacency_map.get(user.current_cell.cell_id, [])
                    adjacent_cells = [cell for cell in cells if cell.cell_id in adjacent_cell_ids and cell.is_active]

                    if adjacent_cells:
                        new_cell = random.choice(adjacent_cells)
                        user.move_to_cell(new_cell)
                    else:
                        print(f"No active adjacent cells for User {user.user_id}.")
                continue

            # Mobilidade normal com interferência
            adjacent_cell_ids = adjacency_map.get(user.current_cell.cell_id, [])
            adjacent_cells = [cell for cell in cells if cell.cell_id in adjacent_cell_ids]
            if adjacent_cells:
                new_cell = random.choice(adjacent_cells)
                user.move_to_cell(new_cell)
                print(f"User {user.user_id} moved to Cell {new_cell.cell_id} with interference level {new_cell.interference_level}")

