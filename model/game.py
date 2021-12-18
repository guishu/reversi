from model.board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.board.set_start_position()
        self.to_play = 0

    def play(self, x, y):
        if self.board.play_token(x, y, self.to_play):
            self.to_play = 1 - self.to_play
            if not self.board.get_valid_moves(self.to_play):
                self.to_play = 1 - self.to_play
