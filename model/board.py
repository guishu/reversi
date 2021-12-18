class Board:
    """
    This is the actual board implementation.
    It holds token collection and handles all the game logic.
    """

    def __init__(self):
        self.size = 8
        self.board = [-1] * 64

    def get_token(self, x, y):
        """
        Retrieves the token at given board coordinates
        :param x: x coordinate
        :param y: y coordinate
        :return: -1 for no token, else player index
        """
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return -1

        return self.board[y * self.size + x]

    def set_token(self, x, y, value):
        """
        Sets the token at given board coordinates without checking game logic
        :param x: x coordinate
        :param y: y coordinate
        :param value: -1 for no token, else player index
        """
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise Exception(f"Wrong coordinate for token: {x}, {y}")

        self.board[y * self.size + x] = value

    def play_token(self, x, y, value):
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise Exception(f"Wrong coordinate for token: {x}, {y}")

        if not self.is_valid_move(x, y, value):
            return False

        self.set_token(x, y, value)
        self._play_direction(x, y, -1, 0, value)
        self._play_direction(x, y, 1, 0, value)
        self._play_direction(x, y, 0, 1, value)
        self._play_direction(x, y, 0, -1, value)

        return True

    def set_start_position(self):
        """
        Initialises the board in a starting game position.
        :return:
        """
        self.board = [-1] * 64
        self.set_token(3, 3, 0)
        self.set_token(4, 4, 0)
        self.set_token(3, 4, 1)
        self.set_token(4, 3, 1)

    def is_valid_move(self, x, y, to_play):
        if self.get_token(x, y) != -1:
            return False

        return (
            self._check_direction(x, y, -1, 0, to_play) or
            self._check_direction(x, y, 1, 0, to_play) or
            self._check_direction(x, y, 0, -1, to_play) or
            self._check_direction(x, y, 0, 1, to_play)
        )

    def _check_direction(self, x, y, dx, dy, to_play):
        cur_x = x + dx
        cur_y = y + dy
        opponent = 1 - to_play
        if self.get_token(cur_x, cur_y) != opponent:
            return False

        while (cur := self.get_token(cur_x, cur_y)) == opponent:
            cur_x += dx
            cur_y += dy

        return cur == to_play

    def _play_direction(self, x, y, dx, dy, to_play):
        if not self._check_direction(x, y, dx, dy, to_play):
            return

        cur_x = x + dx
        cur_y = y + dy
        opponent = 1 - to_play
        while self.get_token(cur_x, cur_y) == opponent:
            self.set_token(cur_x, cur_y, to_play)
            cur_x += dx
            cur_y += dy


