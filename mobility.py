import random

def simulate_mobility(users, cells, adjacency_map, time_steps):
    """
    Simula a mobilidade dos usuários entre células vizinhas com base no mapa de adjacências.
    """
    for t in range(time_steps):
        print(f"Time Step {t}")
        for user in users:
            if user.current_cell:
                # Obter células adjacentes como objetos, não apenas IDs
                adjacent_cell_ids = adjacency_map.get(user.current_cell.cell_id, [])
                adjacent_cells = [cell for cell in cells if cell.cell_id in adjacent_cell_ids]
                if adjacent_cells:
                    new_cell = random.choice(adjacent_cells)
                    user.move_to_cell(new_cell)
            else:
                # Conectar o usuário a uma célula inicial se ainda não estiver conectado
                new_cell = random.choice(cells)
                user.move_to_cell(new_cell)
