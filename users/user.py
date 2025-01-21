class User:
    def __init__(self, user_id, slice_type):
        self.user_id = user_id
        self.slice_type = slice_type  # Tipo de slice (eMBB, URLLC, mMTC)
        self.current_cell = None

    def move_to_cell(self, new_cell):
        if self.current_cell:
            self.current_cell.disconnect_user(self)
        new_cell.connect_user(self)
        self.current_cell = new_cell
