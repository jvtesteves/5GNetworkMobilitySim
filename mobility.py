import random

def simulate_mobility(users, cells, adjacency_map, time_steps):
    for t in range(time_steps):
        print(f"Time Step {t}")

        # Atualizar o status das células (reativar após falha)
        for cell in cells:
            cell.update_status()

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

            # Mobilidade normal
            adjacent_cell_ids = adjacency_map.get(user.current_cell.cell_id, [])
            adjacent_cells = [cell for cell in cells if cell.cell_id in adjacent_cell_ids]
            if adjacent_cells:
                new_cell = random.choice(adjacent_cells)
                user.move_to_cell(new_cell)
