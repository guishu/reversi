class Board:
    def __init__(self):
        self.size = 8
        self.board = [-1] * 64

    def get_token(self, x, y):
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise Exception(f"Wrong coordinate for token: {x}, {y}")

        return self.board[y * self.size + x]

    def set_token(self, x, y, value):
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise Exception(f"Wrong coordinate for token: {x}, {y}")

        self.board[y * self.size + x] = value

    def set_start_position(self):
        self.board = [-1] * 64
        self.set_token(3, 3, 0)
        self.set_token(4, 4, 0)
        self.set_token(3, 4, 1)
        self.set_token(4, 3, 1)